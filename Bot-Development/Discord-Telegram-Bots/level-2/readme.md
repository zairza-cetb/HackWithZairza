# Level 2: Multi-Feature Bots

Build bots with multiple integrated features including external API calls, scheduled tasks, and enhanced user interactions. Focus on asynchronous operations and service integration.

## Project Options

### Option 1: Weather Bot
Bot providing weather information and forecasts.

**Commands:**
- `/weather [city]` - Current weather
- `/forecast [city]` - 5-day forecast
- `/setlocation [city]` - Save default location
- `/temperature [value]` - Convert temperature units

**Features:**
- OpenWeatherMap API integration
- Temperature unit conversion
- Location saving per user
- Weather alerts and emoji

### Option 2: Reminder Bot
Bot for setting and managing reminders.

**Commands:**
- `/remind [time] [message]` - Set reminder
- `/reminders` - List active reminders
- `/cancel [id]` - Cancel reminder
- `/timezone [tz]` - Set timezone

**Features:**
- Natural language time parsing
- Multiple simultaneous reminders
- Timezone support
- Notification delivery

### Option 3: Utility Bot
Multi-purpose bot with various tools.

**Commands:**
- `/calculate [expression]` - Math calculator
- `/translate [text]` - Language translation
- `/shorten [url]` - URL shortener
- `/qr [text]` - Generate QR code

**Features:**
- Expression evaluation
- Translation API integration
- URL shortening service
- QR code generation

## Implementation Example
```
import discord
from discord.ext import commands, tasks
import aiohttp
import asyncio
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

Store reminders
reminders = []

@bot.event
async def on_ready():
print(f'{bot.user} is ready!')
check_reminders.start()

@bot.command(name='weather')
async def weather(ctx, *, city: str):
"""Get current weather for a city"""
url = f'http://api.openweathermap.org/data/2.5/weather'
params = {
'q': city,
'appid': WEATHER_API_KEY,
'units': 'metric'
}

text
async with aiohttp.ClientSession() as session:
    async with session.get(url, params=params) as response:
        if response.status == 200:
            data = await response.json()
            temp = data['main']['temp']
            desc = data['weather']['description']
            
            embed = discord.Embed(
                title=f'Weather in {city.title()}',
                description=f'{desc.title()}',
                color=discord.Color.blue()
            )
            embed.add_field(name='Temperature', value=f'{temp}°C')
            embed.add_field(name='Humidity', value=f"{data['main']['humidity']}%")
            
            await ctx.send(embed=embed)
        else:
            await ctx.send('City not found!')
@bot.command(name='remind')
async def remind(ctx, time: int, *, message: str):
"""Set a reminder (time in minutes)"""
reminder_time = datetime.now() + timedelta(minutes=time)
reminders.append({
'user': ctx.author.id,
'channel': ctx.channel.id,
'time': reminder_time,
'message': message
})

text
await ctx.send(f'⏰ Reminder set for {time} minutes from now!')
@tasks.loop(seconds=30)
async def check_reminders():
"""Check and send due reminders"""
now = datetime.now()
due_reminders = [r for r in reminders if r['time'] <= now]

text
for reminder in due_reminders:
    channel = bot.get_channel(reminder['channel'])
    user = await bot.fetch_user(reminder['user'])
    
    await channel.send(
        f'{user.mention} 🔔 Reminder: {reminder["message"]}'
    )
    reminders.remove(reminder)
@bot.command(name='calculate')
async def calculate(ctx, , expression: str):
"""Evaluate a mathematical expression"""
try:
# Safe evaluation of simple math expressions
allowed_chars = set('0123456789+-/.()')
if all(c in allowed_chars or c.isspace() for c in expression):
result = eval(expression)
await ctx.send(f'📊 Result: {result}')
else:
await ctx.send('Invalid expression!')
except:
await ctx.send('Error calculating expression!')

bot.run(DISCORD_TOKEN)
```

## Technical Requirements

1. **Async/await patterns** for API calls
2. **External API integration** with error handling
3. **Background tasks** for scheduled operations
4. **Data persistence** for user preferences
5. **Embed messages** for rich formatting

## API Keys Setup

**.env file:**
```
DISCORD_TOKEN=your_token
WEATHER_API_KEY=your_openweather_key
TELEGRAM_TOKEN=your_telegram_token
```


## Dependencies
```
discord.py>=2.3.0
python-telegram-bot>=20.0
aiohttp>=3.9.0
python-dotenv>=1.0.0
requests>=2.31.0
```


## Submission Requirements

Folder `BotName_YourGitHubUsername` containing:

1. `bot.py` - Main bot code
2. `.env.example` - All API key templates
3. `requirements.txt` - Dependencies
4. `README.md` - Complete documentation including:
   - API key acquisition instructions
   - Setup steps
   - Command documentation
   - Feature descriptions

## Resources

- [Discord.py Ext Commands](https://discordpy.readthedocs.io/en/stable/ext/commands/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Aiohttp Documentation](https://docs.aiohttp.org/)
- [Discord.py Tasks](https://discordpy.readthedocs.io/en/stable/ext/tasks/)
