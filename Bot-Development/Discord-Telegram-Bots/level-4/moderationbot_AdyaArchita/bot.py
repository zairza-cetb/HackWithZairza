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

# Setup professional logging
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
    # 1. Initialize database and store it in bot_data for universal access
    db = Database()
    await db.init_db()
    application.bot_data["db"] = db
    
    # 2. Load config and store it in bot_data
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        application.bot_data["config"] = config
        logger.info("Database initialized and config loaded successfully.")
    except FileNotFoundError:
        logger.warning("config.json not found. Creating a default config.")
        default_config = {
            "profanity_words": ["examplecurse"],
            "max_warnings": 3,
            "mod_log_chat_id": None
        }
        with open("config.json", "w") as f:
            json.dump(default_config, f, indent=4)
        application.bot_data["config"] = default_config
    except json.JSONDecodeError:
        logger.error("Error decoding config.json. Please check its format.")
        # Terminate or use a default config
        application.bot_data["config"] = {}


def main() -> None:
    """Load token, build the bot application, set up handlers, and start the bot."""
    # 1. Load bot token from environment variables
    load_dotenv()
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not TOKEN:
        logger.critical("TELEGRAM_BOT_TOKEN not found in .env file. Exiting.")
        return

    # 2. Build the bot application, including the post_init hook
    application = ApplicationBuilder().token(TOKEN).post_init(post_init).build()

    # 3. Register the global error handler
    application.add_error_handler(error_handler)

    # 4. Register ALL command and message handlers
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
    
    # Add the profanity filter for all text messages that are not commands
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mod_handlers.profanity_filter))

    logger.info("Bot is starting up...")
    
    # 5. Start the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Bot shutting down gracefully.")
    except Exception as e:
        logger.critical(f"An unexpected error occurred: {e}", exc_info=True)

