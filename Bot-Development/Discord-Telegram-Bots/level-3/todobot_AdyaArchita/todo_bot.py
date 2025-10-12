import logging
import os
from dotenv import load_dotenv
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.constants import ParseMode
import database as db

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    welcome_message = (
        f"Hi {user.first_name}! I'm your personal Todo List Bot.\n"
        "You can manage your tasks using the `/todo` command.\n"
        "Try `/todo help` to see all available options."
    )
    await update.message.reply_text(welcome_message)

async def todo_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await list_tasks(update, context)
        return

    subcommand = context.args[0].lower()
    args = context.args[1:]

    if subcommand == "add":
        await add_task(update, context, args)
    elif subcommand == "list":
        await list_tasks(update, context)
    elif subcommand == "complete":
        await complete_task(update, context, args)
    elif subcommand == "delete":
        await delete_task(update, context, args)
    elif subcommand == "clear":
        await clear_tasks(update, context)
    elif subcommand == "help":
        await show_help(update, context)
    else:
        await update.message.reply_text(
            f"Unknown command '{subcommand}'. Use `/todo help` to see available commands."
        )
async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE, args: list) -> None:
    user_id = update.effective_user.id
    if not args:
        await update.message.reply_text("Please provide a task to add. Usage: `/todo add [your task]`")
        return
    task_text = " ".join(args)
    
    if len(task_text) > 255:
        await update.message.reply_text("Task is too long. Please keep it under 255 characters.")
        return
    await db.add_task(user_id=user_id, task=task_text)
    await update.message.reply_text(f"✅ Task added: '{task_text}'")

async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    tasks = await db.get_tasks(user_id)
    if not tasks:
        await update.message.reply_text("You have no tasks! Add one with `/todo add [your task]`.")
        return
    message = "<b>Your Todo List:</b>\n"
    for task in tasks:
        task_id, task_text, completed = task
        status_emoji = "✅" if completed else "⬜️"
        task_display = f"<s>{task_text}</s>" if completed else task_text
        message += f"{status_emoji} `[{task_id}]` {task_display}\n"
    await update.message.reply_html(message)

async def complete_task(update: Update, context: ContextTypes.DEFAULT_TYPE, args: list) -> None:
    """Marks a task as complete."""
    user_id = update.effective_user.id
    if not args:
        await update.message.reply_text("Please provide a task ID to complete. Usage: `/todo complete [id]`")
        return

    try:
        task_id = int(args[0])
    except ValueError:
        await update.message.reply_text("Invalid ID. Please provide a number.")
        return

    rows_affected = await db.update_task_status(task_id=task_id, user_id=user_id, completed=True)

    if rows_affected > 0:
        await update.message.reply_text(f"🎉 Task `{task_id}` marked as complete!")
    else:
        await update.message.reply_text(f"Task with ID `{task_id}` not found or you don't have permission to change it.")

async def delete_task(update: Update, context: ContextTypes.DEFAULT_TYPE, args: list) -> None:
    user_id = update.effective_user.id
    if not args:
        await update.message.reply_text("Please provide a task ID to delete. Usage: `/todo delete [id]`")
        return
        
    try:
        task_id = int(args[0])
    except ValueError:
        await update.message.reply_text("Invalid ID. Please provide a number.")
        return

    rows_affected = await db.delete_task(task_id=task_id, user_id=user_id)
    
    if rows_affected > 0:
        await update.message.reply_text(f"🗑️ Task `{task_id}` deleted.")
    else:
        await update.message.reply_text(f"Task with ID `{task_id}` not found or you don't have permission to delete it.")

async def clear_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    await db.clear_tasks(user_id)
    await update.message.reply_text("💥 All your tasks have been cleared.")

async def show_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "<b>Todo Bot Commands:</b>\n\n"
        "• `/todo add [task]` - Add a new task.\n"
        "• `/todo list` or `/todo` - Show all your tasks.\n"
        "• `/todo complete [id]` - Mark a task as complete.\n"
        "• `/todo delete [id]` - Remove a task.\n"
        "• `/todo clear` - Delete all of your tasks.\n"
        "• `/todo help` - Show this help message."
    )
    await update.message.reply_html(help_text)

def main() -> None:
    """Start the bot."""
    if not TELEGRAM_TOKEN:
        logger.error("TELEGRAM_TOKEN not found in .env file.")
        return

    logger.info("Initializing database...")
    asyncio.run(db.init_db())
    logger.info("Database initialized successfully.")
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("todo", todo_command))

    logger.info("Bot is starting...")
    application.run_polling()

if __name__ == "__main__":
    main()
