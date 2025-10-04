import os
import logging
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update, Bot
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# --- Command Handlers ---
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a dynamic welcome message when the /start command is issued."""
    user = update.effective_user
    welcome_message = (
        f"Hi, {user.first_name}! Welcome to the Greeting Bot. ✨\n\n"
        "I'm here to make things a bit more friendly. "
        "You can use `/help` to see all the commands I know."
    )
    await update.message.reply_text(welcome_message)

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responds with a simple greeting."""
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"Hello, {user_name}! 👋 How can I help you today?")

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays information about the bot."""
    bot_info = (
        "🤖 **Greeting Bot by Adya **\n"
        "I am a friendly bot who is on a mission to make your day brighter 😊 .\n"
        "I am designed to greet users, provide basic info, and handle simple commands . I can only perform simple interactions. \n"
        " Use `/help` to see what I can do! Please be kind to me (I am still learning). "
    )
    await update.message.reply_text(bot_info, parse_mode=ParseMode.MARKDOWN)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays a list of available commands."""
    help_text = (
        "Here are the commands you can use:\n\n"
        "*/start* - Get the welcome message.\n"
        "*/hello* - Get a friendly greeting.\n"
        "*/info* - Learn more about me.\n"
        "*/time* - See the current server time.\n"
        "*/echo <text>* - I will repeat your message back to you.\n"
        "*/help* - Show this help message.\n\n"
        "I also welcome new members, say goodbye when they leave, and respond if you @mention me!"
    )
    await update.message.reply_text(help_text, parse_mode=ParseMode.MARKDOWN)

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Shows the current server time."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await update.message.reply_text(f"The current server time is: {current_time} 🕰️")

async def echo_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Repeats the user's message back to them."""
    if context.args:
        message_to_echo = ' '.join(context.args)
        await update.message.reply_text(f"{message_to_echo}")
    else:
        await update.message.reply_text("Please provide a message for me to echo! \nExample: `/echo Hello World`")

async def welcome_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message to new members."""
    for new_member in update.message.new_chat_members:
        user_name = new_member.first_name
        chat_title = update.message.chat.title
        welcome_text = (
            f"Welcome, {user_name}! 🎉\n"
            f"Glad to have you in **{chat_title}**. Feel free to say hello!"
        )
        await update.message.reply_text(welcome_text, parse_mode=ParseMode.MARKDOWN)

async def goodbye_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message when a user leaves the group."""
    left_user = update.message.left_chat_member
    if left_user:
        user_name = left_user.first_name
        await update.message.reply_text(f"Goodbye dear , {user_name} 😢 ! It was fun with you around here . We'll miss you. ")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles messages with a robust method for getting the bot's username."""
    message = update.message
    if not message.text:
        return
        
    message_text = message.text.lower()
    bot_username = context.bot_data.get('username')
    if not bot_username:
        bot_info = await context.bot.get_me()
        bot_username = bot_info.username.lower()
        context.bot_data['username'] = bot_username

    greeting_keywords = ['hi', 'hello', 'hey']
    if any(word in message_text for word in greeting_keywords) and f"@{bot_username}" in message_text:
        user_name = message.from_user.first_name
        await message.reply_text(f"Hello back, {user_name}! 👋")
        return

    if f"@{bot_username}" in message_text:
        await message.reply_text("You mentioned me! Need help? Try the `/help` command. 😊")
        return

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main() -> None:
    """Start the bot."""
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("hello", hello_command))
    application.add_handler(CommandHandler("info", info_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("time", time_command))
    application.add_handler(CommandHandler("echo", echo_command))
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_message))
    application.add_handler(MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, goodbye_message))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_error_handler(error_handler)

    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()