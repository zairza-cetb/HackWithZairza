# decorators.py
from functools import wraps
from telegram import Update
from telegram.ext import ContextTypes

def is_admin(func):
    """Custom decorator to check if the command user is an admin in the chat."""
    @wraps(func)
    async def wrapped(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        if update.effective_chat.type == 'private':
            await update.message.reply_text("This command can only be used in groups.")
            return

        user_id = update.effective_user.id
        chat_admins = await context.bot.get_chat_administrators(update.effective_chat.id)
        admin_ids = {admin.user.id for admin in chat_admins}
        
        if user_id not in admin_ids:
            await update.message.reply_text("⛔️ You must be a group admin to use this command.")
            return
        
        return await func(update, context, *args, **kwargs)
    return wrapped

