# weather_bot.py

import logging
import asyncio
import aiohttp
import json
from datetime import datetime
from dotenv import load_dotenv
import os
import html
import traceback

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    CallbackQueryHandler,
    filters
)
from telegram.constants import ParseMode
from telegram.helpers import escape_markdown

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

USER_DATA_FILE = "user_locations.json"

def load_user_data():
    """Loads user location data from a JSON file."""
    try:
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_user_data(data):
    """Saves user location data to a JSON file."""
    with open(USER_DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

user_locations = load_user_data()

async def get_weather_data(city: str, endpoint: str = "weather"):
    """
    Fetches weather data from OpenWeatherMap API asynchronously.
    Endpoints: 'weather' for current, 'forecast' for 5-day.
    """
    base_url = "http://api.openweathermap.org/data/2.5/"
    params = {"q": city, "appid": WEATHER_API_KEY, "units": "metric"}
    url = f"{base_url}{endpoint}"

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, params=params) as response:
                response.raise_for_status() 
                return await response.json()
        except aiohttp.ClientResponseError as e:
            logger.error(f"API request failed for {city}: {e.status} {e.message}")
            if e.status == 404:
                return {"cod": "404", "message": "City not found."}
            return {"cod": str(e.status), "message": "An API error occurred."}
        except aiohttp.ClientError as e:
            logger.error(f"AIOHTTP client error for {city}: {e}")
            return {"cod": "500", "message": "A network error occurred."}
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return {"cod": "500", "message": "An unexpected error occurred."}

def get_weather_emoji(weather_id):
    """Returns an emoji corresponding to the weather condition ID."""
    if 200 <= weather_id < 300: return "⛈️"  
    if 300 <= weather_id < 400: return "🌦️"  
    if 500 <= weather_id < 600: return "🌧️"  
    if 600 <= weather_id < 700: return "❄️"  
    if 700 <= weather_id < 800: return "🌫️"  
    if weather_id == 800: return "☀️"       
    if 801 <= weather_id < 805: return "☁️" 
    return "🌍" 

def format_current_weather(data, city):
    """Formats the current weather data into a readable string for MarkdownV2."""
    city_escaped = escape_markdown(city, version=2)
    if not data or data.get("cod") != 200:
        error_message = data.get('message', 'An unknown error occurred')
        return f"Sorry, I couldn't retrieve the weather for *{city_escaped}*\\. {escape_markdown(error_message, version=2)}"

    main = data["main"]
    weather = data["weather"][0]
    wind = data["wind"]
    emoji = get_weather_emoji(weather["id"])
    description = escape_markdown(weather['description'].title(), version=2)
    temp = str(main['temp']).replace('.', '\\.')
    feels_like = str(main['feels_like']).replace('.', '\\.')
    message = (
        f"*{city_escaped} Weather* {emoji}\n\n"
        f"🌡️ *Temperature:* {temp}°C \\(Feels like: {feels_like}°C\\)\n"
        f"📊 *Condition:* {description}\n"
        f"💧 *Humidity:* {main['humidity']}%\n"
        f"💨 *Wind Speed:* {escape_markdown(str(wind['speed']), version=2)} m/s\n"
        f"📈 *Pressure:* {main['pressure']} hPa\n"
    )
    return message

def format_forecast(data, city):
    """Formats the 5-day forecast data into a readable string for MarkdownV2."""
    city_escaped = escape_markdown(city.title(), version=2)
    if not data or data.get("cod") != "200":
         error_message = data.get('message', 'An unknown error occurred')
         return f"Sorry, I couldn't retrieve the forecast for *{city_escaped}*\\. {escape_markdown(error_message, version=2)}"

    message = f"*5\\-Day Weather Forecast for {city_escaped}*\n\n"
    daily_forecasts = {}
    for item in data["list"]:
        date = datetime.fromtimestamp(item["dt"]).strftime("%Y-%m-%d")
        if date not in daily_forecasts:
            daily_forecasts[date] = []
        daily_forecasts[date].append(item)
    
    count = 0
    for date, items in sorted(daily_forecasts.items()):
        if count >= 5:
            break
        rep_item = next((item for item in items if "12:00:00" in item["dt_txt"]), items[0])
        day_name = escape_markdown(datetime.strptime(date, "%Y-%m-%d").strftime("%A, %b %d"), version=2)
        temp_min = str(round(min(i['main']['temp_min'] for i in items), 1)).replace('.', '\\.')
        temp_max = str(round(max(i['main']['temp_max'] for i in items), 1)).replace('.', '\\.')
        weather = rep_item['weather'][0]
        emoji = get_weather_emoji(weather['id'])
        description = escape_markdown(weather['description'].title(), version=2)

        message += (
            f"*{day_name}* {emoji}\n"
            f"  `{description}`\n"
            f"  🌡️ Temp: {temp_min}°C / {temp_max}°C\n\n"
        )
        count += 1
    return message

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message when the /start command is issued."""
    user = update.effective_user
    welcome_message = (
        f"Hi {user.mention_markdown_v2()}\\! I'm your friendly Weather Bot\\.\n\n"
        "Here's what I can do:\n"
        "`/weather [city]` \\- Get the current weather\\.\n"
        "`/forecast [city]` \\- Get a 5\\-day forecast\\.\n"
        "`/setlocation [city]` \\- Set your default city\\.\n"
        "`/temperature <value> [C/F]` \\- Convert temperatures \\(C to F, F to C\\)\\.\n"
        "`/help` \\- Show this message again\\."
    )
    await update.message.reply_markdown_v2(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends help message."""
    help_text = (
        "*Weather Bot Commands*\n\n"
        "`/weather [city]`\n_Get the current weather for a specific city\\. If no city is provided, uses your saved location\\._\n\n"
        "`/forecast [city]`\n_Get the 5\\-day weather forecast\\._\n\n"
        "`/setlocation [city]`\n_Saves a city as your default location for quick weather checks\\._\n\n"
        "`/temperature <value> [C/F]`\n_Converts a temperature value\\. Default is Celsius to Fahrenheit\\. Use 'F' for Fahrenheit to Celsius\\._"
    )
    await update.message.reply_markdown_v2(help_text)

async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Fetches and sends the current weather."""
    user_id = str(update.effective_user.id)
    city = " ".join(context.args) if context.args else user_locations.get(user_id)
    if not city:
        await update.message.reply_text("Please specify a city or set a default location with /setlocation [city].")
        return
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    weather_data = await get_weather_data(city, "weather")
    message = format_current_weather(weather_data, city)
    await update.message.reply_markdown_v2(message)

async def forecast_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Fetches and sends the 5-day weather forecast."""
    user_id = str(update.effective_user.id)
    city = " ".join(context.args) if context.args else user_locations.get(user_id)
    if not city:
        await update.message.reply_text("Please specify a city or set a default location with /setlocation [city].")
        return
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    forecast_data = await get_weather_data(city, "forecast")
    message = format_forecast(forecast_data, city)
    await update.message.reply_markdown_v2(message)

async def setlocation_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sets the user's default location."""
    user_id = str(update.effective_user.id)
    if not context.args:
        await update.message.reply_text("Please specify a city to set as your default location. Usage: /setlocation [city]")
        return
    city = " ".join(context.args)
    user_locations[user_id] = city
    save_user_data(user_locations)
    await update.message.reply_text(f"Your default location has been set to {city.title()}.")
async def temperature_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Converts temperature between Celsius and Fahrenheit."""
    if not context.args:
        await update.message.reply_text(
            "Usage: /temperature <value> [C/F]\n"
            "Example: `/temperature 32 C` or `/temperature 98.6 F`"
        )
        return
    try:
        value = float(context.args[0])
        unit = 'C'  
        if len(context.args) > 1 and context.args[1].upper() == 'F':
            unit = 'F'
        if unit == 'C':
            celsius = value
            fahrenheit = (celsius * 9/5) + 32
            celsius_escaped = str(celsius).replace('.', '\\.')
            fahrenheit_escaped = f"{fahrenheit:.1f}".replace('.', '\\.')
            await update.message.reply_markdown_v2(f"{celsius_escaped}°C is equal to {fahrenheit_escaped}°F\\.")
        else:  
            fahrenheit = value
            celsius = (fahrenheit - 32) * 5/9
            fahrenheit_escaped = str(fahrenheit).replace('.', '\\.')
            celsius_escaped = f"{celsius:.1f}".replace('.', '\\.')
            await update.message.reply_markdown_v2(f"{fahrenheit_escaped}°F is equal to {celsius_escaped}°C\\.")
    except ValueError:
        await update.message.reply_text("Invalid number. Please provide a valid temperature value.")

async def weather_alert_task(context: ContextTypes.DEFAULT_TYPE):
    """Example of a scheduled task. This can be expanded for actual alerts."""
    logger.info("Scheduled weather check running...")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message to notify the developer."""
    logger.error("Exception while handling an update:", exc_info=context.error)
    tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
    tb_string = "".join(tb_list)
    update_str = update.to_dict() if isinstance(update, Update) else str(update)
    message = (
        f"An exception was raised while handling an update\n"
        f"<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}"
        "</pre>\n\n"
        f"<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n\n"
        f"<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n\n"
        f"<pre>{html.escape(tb_string)}</pre>"
    )
    if update and hasattr(update, 'effective_chat') and update.effective_chat:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="Sorry, an error occurred while processing your request.", parse_mode=ParseMode.HTML
        )

def main() -> None:
    """Start the bot."""
    if not TELEGRAM_TOKEN or not WEATHER_API_KEY:
        logger.error("API keys not found in .env file. Please set TELEGRAM_TOKEN and WEATHER_API_KEY.")
        return

    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_error_handler(error_handler)
    job_queue = application.job_queue
    job_queue.run_repeating(weather_alert_task, interval=3600, first=10)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("weather", weather_command))
    application.add_handler(CommandHandler("forecast", forecast_command))
    application.add_handler(CommandHandler("setlocation", setlocation_command))
    application.add_handler(CommandHandler("temperature", temperature_command))
    logger.info("Bot is starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

