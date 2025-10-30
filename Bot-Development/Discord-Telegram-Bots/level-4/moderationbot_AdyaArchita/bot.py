import os
import json
import logging
import traceback
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.error import TelegramError

from database import Database
import handlers.moderation as mod_handlers

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Logs the error and sends a message to the user if possible."""
    logger.error("Exception while handling an update:", exc_info=context.error)

    # Format the traceback for logging
    tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
    tb_string = "".join(tb_list)
    logger.error(tb_string)

    # Attempt to send a user-friendly message back to the chat
    if isinstance(update, Update) and update.effective_message:
        try:
            await update.effective_message.reply_text(
                "An unexpected error occurred. The bot administrators have been notified."
            )
        except TelegramError as e:
            logger.error(f"Could not send error message to user: {e}")


async def post_init(application: Application) -> None:
    """
    Post-initialization hook for the bot.
    Initializes the database and loads config, storing them in the application context.
    """
    db = Database()
    await db.init_db()
    application.bot_data["db"] = db

    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        application.bot_data["config"] = config
        logger.info("Database initialized and config loaded successfully.")
    except FileNotFoundError:
        logger.warning("config.json not found. Creating a default config.")

        default_config = {
            "mod_log_chat_id": 0,
            "banned_words": ["example_profanity", "spam_word"],
            "super_admin_ids": [],
            "database_path": "moderation.db",
            "backup_directory": "./backups"
        }
        with open("config.json", "w") as f:
            json.dump(default_config, f, indent=4)
        application.bot_data["config"] = default_config
    except json.JSONDecodeError as e:

        logger.exception("Error decoding config.json. Please check its format. Bot is shutting down.")
        raise SystemExit("Invalid config.json format. Bot cannot start.") from e


def main() -> None:
    """Load token, build the bot application, set up handlers, and start the bot."""
    load_dotenv()
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not TOKEN:
        logger.critical("TELEGRAM_BOT_TOKEN not found in .env file. Exiting.")
        return

    application = ApplicationBuilder().token(TOKEN).post_init(post_init).build()
    application.add_error_handler(error_handler)
    application.add_handler(CommandHandler("warn", mod_handlers.warn))
    application.add_handler(CommandHandler("warnings", mod_handlers.warnings))
    application.add_handler(CommandHandler("rmwarn", mod_handlers.rmwarn))
    application.add_handler(CommandHandler("kick", mod_handlers.kick))
    application.add_handler(CommandHandler("ban", mod_handlers.ban))
    application.add_handler(CommandHandler("unban", mod_handlers.unban))
    application.add_handler(CommandHandler("mute", mod_handlers.mute))
    application.add_handler(CommandHandler("unmute", mod_handlers.unmute))
    application.add_handler(CommandHandler("purge", mod_handlers.purge))
    application.add_handler(CommandHandler("clean", mod_handlers.clean))
 
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mod_handlers.profanity_filter))
    logger.info("Bot is starting up...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Bot shutting down gracefully.")
    except Exception as e:
        logger.critical(f"An unexpected error occurred: {e}", exc_info=True)
