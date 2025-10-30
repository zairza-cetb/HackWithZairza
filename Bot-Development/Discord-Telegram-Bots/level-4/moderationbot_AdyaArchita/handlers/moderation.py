import datetime
import asyncio
import html  # Import the html module for escaping
from typing import Tuple
from telegram import Update, ChatPermissions
from telegram.ext import ContextTypes
from telegram.constants import ParseMode
from telegram.error import BadRequest, TelegramError 

from decorators import is_admin

#  Helper Functions 

def get_target_user_and_reason(update: Update, context: ContextTypes.DEFAULT_TYPE) -> Tuple[object, str] | Tuple[None, None]:
    """
    A helper to extract the target user from a reply and the reason from command arguments.
    Returns (None, None) if the command is not a reply.
    """
    if not update.message.reply_to_message:
        return None, None
    
    target_user = update.message.reply_to_message.from_user
    reason = " ".join(context.args) if context.args else "No reason provided."
    return target_user, reason

def parse_duration(duration_str: str) -> datetime.timedelta | None:
    """Parses a duration string (e.g., 1d, 2h, 30m) into a timedelta object."""
    if not duration_str:
        return None
    unit = duration_str[-1].lower()
    try:
        value = int(duration_str[:-1])
        if unit == 'm':
            return datetime.timedelta(minutes=value)
        elif unit == 'h':
            return datetime.timedelta(hours=value)
        elif unit == 'd':
            return datetime.timedelta(days=value)
    except (ValueError, IndexError):
        return None
    return None

async def log_action(context: ContextTypes.DEFAULT_TYPE, message: str):
    """Sends a log message to the configured log chat."""
    log_chat_id = context.bot_data.get("config", {}).get("mod_log_chat_id")
    if log_chat_id:
        try:
            await context.bot.send_message(chat_id=log_chat_id, text=message, parse_mode=ParseMode.HTML)
        except Exception as e:
            print(f"Failed to send log message: {e}")

# Core Moderation Commands 

@is_admin
async def warn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Warns a user. Usage: /warn [reason] (in reply)."""
    db = context.bot_data['db']
    target_user, reason = get_target_user_and_reason(update, context)
    if not target_user:
        await update.message.reply_text("Error: Please use this command by replying to the user you want to warn.")
        return

    moderator = update.effective_user
    new_warning_id, total_warnings = await db.add_warning(target_user.id, update.effective_chat.id, moderator.id, reason)
    
    safe_reason = html.escape(reason)  #  Escape HTML
    
    response = (
        f"<b>⚠️ User Warned</b> (Warning #{total_warnings})\n\n"
        f"<b>User:</b> {target_user.mention_html()} (<code>{target_user.id}</code>)\n"
        f"<b>Moderator:</b> {moderator.mention_html()}\n"
        f"<b>Reason:</b> <code>{safe_reason}</code>"  #  Use safe reason
    )
    await update.message.reply_html(response)
    await log_action(context, response)

@is_admin
async def warnings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Shows all warnings for a user. Usage: /warnings (in reply)."""
    db = context.bot_data['db']
    target_user, _ = get_target_user_and_reason(update, context)
    if not target_user:
        await update.message.reply_text("Error: Please reply to a user to see their warnings.")
        return
    
    user_warnings = await db.get_warnings(target_user.id, update.effective_chat.id)

    if not user_warnings:
        await update.message.reply_html(f"✅ User {target_user.mention_html()} has no warnings.")
        return

    response = f"<b>📜 Warning history for {target_user.mention_html()}:</b>\n\n"
    for row in user_warnings:
        warn_id, _, _, mod_id, reason, ts = row
        safe_reason = html.escape(reason)  #  Escape reason from DB
        response += f"<b>ID: {warn_id}</b> | <b>Reason:</b> <code>{safe_reason}</code>\n(<i>on {ts.split(' ')[0]}</i>)\n\n"
    await update.message.reply_html(response)

@is_admin
async def rmwarn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Removes a specific warning by its ID. Usage: /rmwarn <warning_id>."""
    db = context.bot_data['db']
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Usage: /rmwarn <warning_id>")
        return
    
    warning_id = int(context.args[0])
    was_removed = await db.remove_warning(warning_id)

    if was_removed:
        response = f"✅ Warning ID <code>{warning_id}</code> has been removed."
    else:
        response = f"❌ Could not find a warning with ID <code>{warning_id}</code>."
    
    await update.message.reply_html(response)
    await log_action(context, response)


@is_admin
async def kick(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Kicks a user. Usage: /kick [reason] (in reply)."""
    target_user, reason = get_target_user_and_reason(update, context)
    if not target_user:
        await update.message.reply_text("Error: Reply to a user to kick them.")
        return
    
    moderator = update.effective_user
    try:
        await context.bot.ban_chat_member(chat_id=update.effective_chat.id, user_id=target_user.id)
        await context.bot.unban_chat_member(chat_id=update.effective_chat.id, user_id=target_user.id)
        safe_reason = html.escape(reason)  
        
        response = (
            f"<b>👢 User Kicked</b>\n\n"
            f"<b>User:</b> {target_user.mention_html()} (<code>{target_user.id}</code>)\n"
            f"<b>Moderator:</b> {moderator.mention_html()}\n"
            f"<b>Reason:</b> <code>{safe_reason}</code>" 
        )
        await update.message.reply_html(response)
        await log_action(context, response)
    except BadRequest as e:
        await update.message.reply_text(f"Error: {e.message}")

@is_admin
async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bans a user. Usage: /ban [duration] [reason] (in reply)."""
    target_user, _ = get_target_user_and_reason(update, context) 
    if not target_user:
        await update.message.reply_text("Error: Reply to a user to ban them.")
        return

    moderator = update.effective_user
    duration_str = context.args[0] if context.args else None
    duration = parse_duration(duration_str)
    reason = " ".join(context.args[1:]) if duration else " ".join(context.args)
    if not reason: reason = "No reason specified."
    
    until_date = datetime.datetime.now(datetime.timezone.utc) + duration if duration else None

    try:
        await context.bot.ban_chat_member(
            chat_id=update.effective_chat.id, 
            user_id=target_user.id,
            until_date=until_date
        )
        duration_text = f"for {duration_str}" if duration else "permanently"
        safe_reason = html.escape(reason)  
        
        response = (
            f"<b>🚫 User Banned {duration_text}</b>\n\n"
            f"<b>User:</b> {target_user.mention_html()} (<code>{target_user.id}</code>)\n"
            f"<b>Moderator:</b> {moderator.mention_html()}\n"
            f"<b>Reason:</b> <code>{safe_reason}</code>"  
        )
        await update.message.reply_html(response)
        await log_action(context, response)
    except BadRequest as e:
        await update.message.reply_text(f"Error: {e.message}")

@is_admin
async def unban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Unbans a user by their ID. Usage: /unban <user_id>."""
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Usage: /unban <user_id>")
        return
    
    user_id_to_unban = int(context.args[0])
    moderator = update.effective_user
    
    try:
        await context.bot.unban_chat_member(chat_id=update.effective_chat.id, user_id=user_id_to_unban)
        response = (
            f"<b>✅ User Unbanned</b>\n\n"
            f"<b>User ID:</b> <code>{user_id_to_unban}</code>\n"
            f"<b>Moderator:</b> {moderator.mention_html()}"
        )
        await update.message.reply_html(response)
        await log_action(context, response)
    except BadRequest as e:
        await update.message.reply_text(f"Error: {e.message}")


@is_admin
async def mute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mutes a user. Usage: /mute [duration] [reason] (in reply)."""
    target_user, _ = get_target_user_and_reason(update, context)
    if not target_user:
        await update.message.reply_text("Error: Reply to a user to mute them.")
        return

    moderator = update.effective_user
    duration_str = context.args[0] if context.args else None
    duration = parse_duration(duration_str)
    reason = " ".join(context.args[1:]) if duration else " ".join(context.args)
    if not reason: reason = "No reason specified."

    until_date = datetime.datetime.now(datetime.timezone.utc) + duration if duration else None
    permissions = ChatPermissions(can_send_messages=False)

    try:
        await context.bot.restrict_chat_member(
            chat_id=update.effective_chat.id,
            user_id=target_user.id,
            permissions=permissions,
            until_date=until_date
        )
        duration_text = f"for {duration_str}" if duration else "permanently"
        safe_reason = html.escape(reason)
        
        response = (
            f"<b>🔇 User Muted {duration_text}</b>\n\n"
            f"<b>User:</b> {target_user.mention_html()} (<code>{target_user.id}</code>)\n"
            f"<b>Moderator:</b> {moderator.mention_html()}\n"
            f"<b>Reason:</b> <code>{safe_reason}</code>"
        )
        await update.message.reply_html(response)
        await log_action(context, response)
    except BadRequest as e:
        await update.message.reply_text(f"Error: {e.message}")

@is_admin
async def unmute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Unmutes a user. Usage: /unmute (in reply)."""
    target_user, _ = get_target_user_and_reason(update, context)
    if not target_user:
        await update.message.reply_text("Error: Reply to a user to unmute them.")
        return

    moderator = update.effective_user
    permissions = ChatPermissions(
        can_send_messages=True, can_send_audios=True, can_send_documents=True,
        can_send_photos=True, can_send_videos=True, can_send_video_notes=True,
        can_send_voice_notes=True, can_send_polls=True, can_send_other_messages=True,
        can_add_web_page_previews=True, can_invite_users=True
    )

    try:
        await context.bot.restrict_chat_member(
            chat_id=update.effective_chat.id,
            user_id=target_user.id,
            permissions=permissions
        )
        response = (
            f"<b>🔊 User Unmuted</b>\n\n"
            f"<b>User:</b> {target_user.mention_html()} (<code>{target_user.id}</code>)\n"
            f"<b>Moderator:</b> {moderator.mention_html()}"
        )
        await update.message.reply_html(response)
        await log_action(context, response)
    except BadRequest as e:
        await update.message.reply_text(f"Error: {e.message}")

@is_admin
async def purge(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Deletes all messages from the replied-to message up to the command."""
    if not update.message.reply_to_message:
        await update.message.reply_text("Reply to a message to start purging from.")
        return

    start_message_id = update.message.reply_to_message.message_id
    end_message_id = update.message.message_id
    chat_id = update.effective_chat.id
    
    deleted_count = 0
    for message_id in range(start_message_id, end_message_id + 1):
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
            deleted_count += 1
        except BadRequest:
            pass # Message might be too old or already deleted
    
    response_msg = await update.message.reply_text(f"✅ Purged {deleted_count} messages.")
    await asyncio.sleep(5)
    await context.bot.delete_message(chat_id=chat_id, message_id=response_msg.message_id)

@is_admin
async def clean(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Deletes a specified number of recent messages. Usage: /clean <number>"""
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Usage: /clean <number>")
        return

    try:
        num_to_delete = int(context.args[0])
        if not (1 < num_to_delete <= 100):
            await update.message.reply_text("Please provide a number between 2 and 100.")
            return
    except (ValueError, IndexError):
        await update.message.reply_text("Invalid number. Usage: /clean <number>")
        return

    chat_id = update.effective_chat.id
    start_message_id = update.message.message_id
    deleted_count = 0

    # Loop backwards from the current message and delete.
    # This is more reliable than calculating message IDs.
    for i in range(num_to_delete):
        message_id_to_delete = start_message_id - i
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id_to_delete)
            deleted_count += 1
        except BadRequest:
            # This handles cases where the message doesn't exist, is too old, or we lack permissions.
            pass
    
    response_msg = await context.bot.send_message(
        chat_id=chat_id, 
        text=f"✅ Cleaned up {deleted_count} messages."
    )
    # Delete the confirmation message after a few seconds.
    await asyncio.sleep(5)
    await context.bot.delete_message(chat_id=chat_id, message_id=response_msg.message_id)


async def profanity_filter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Auto-moderation filter for banned words."""
    if not update.message or not update.message.text: return
    
    # Do not moderate admins
    try:
        chat_admins = await context.bot.get_chat_administrators(update.effective_chat.id)
        if update.effective_user.id in {admin.user.id for admin in chat_admins}: return
    except TelegramError:
        pass # Don't filter if we can't check admin status

    #  Use "banned_words" to match config 
    banned_words = context.bot_data.get("config", {}).get("banned_words", [])
    message_text_lower = update.message.text.lower()
    
    if any(word in message_text_lower for word in banned_words):
        try:
            await update.message.delete()
            # Optionally, send a warning message that deletes itself
            warn_msg = await update.message.reply_text(
                f"Watch your language, {update.effective_user.mention_html()}.",
                parse_mode=ParseMode.HTML
            )
            await asyncio.sleep(5)
            await warn_msg.delete()
        except Exception as e:
            print(f"Failed to delete profane message: {e}")

