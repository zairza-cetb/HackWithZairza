# Level 1: Basic Command Bots

Create simple bots that respond to basic commands and user interactions. Focus on bot setup, authentication, and fundamental command handling patterns.

## Project Options

### Option 1: Greeting Bot
Bot that responds to greetings and basic interactions.

**Commands:**
- `/hello` - Responds with greeting message
- `/info` - Displays bot information
- `/help` - Shows available commands
- `/time` - Shows current server time

**Features:**
- Welcome messages for new members
- Response to mentions
- Basic command parsing
- Help documentation

### Option 2: Dice Roller Bot
Interactive dice rolling bot for gaming communities.

**Commands:**
- `/roll` - Rolls a single six-sided die
- `/roll 2d6` - Rolls two six-sided dice
- `/roll 1d20` - Rolls twenty-sided die
- `/flip` - Flips a coin

**Features:**
- Parse dice notation (XdY format)
- Display roll results with total
- Support multiple dice types
- Random number generation

### Option 3: Quote Bot
Bot that shares random quotes or facts.

**Commands:**
- `/quote` - Shares random quote
- `/fact` - Shares random fact
- `/joke` - Tells a random joke
- `/inspire` - Shares inspirational message

**Features:**
- Quote database (hardcoded array)
- Random selection algorithm
- Category filtering
- Daily quote feature

## Implementation Example (Discord)
```
import discord
from discord.ext import commands
import random
import os
load_dotenv()
TOKEN = os.getenv('D

intents = discord.Intents.default()
intents.message_content = True
bot = commands.

@bot.event
async def on_ready():
print(f'{

@bot.command(name='hello')
async def hello(ctx):
"""Responds with a greetin
@bot.command(name='roll')
async def roll_dice(ctx, dice: str = '1d6'):
"""Rolls dice in XdY forma
"""
try: rolls, sides = map(int,
ice.split('d')) results = [random.randint(1, sides
for _ in range(roll
{total}')
exc
pt: await ctx.send('Invalid format. Use: /roll

@bot.command(name='flip')
async def flip_coin(ctx):
"""Flips a coi
""" result = random.choice(['Heads', '
bot.run(TOKEN)
```


## Implementation Example (Telegram)
```
import os
import random
from dotenv import load_dotenv
from telegram import Update
from telegram.ext i

load_dotenv()
TOKEN = os.getenv('TE

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
"""Send welcome messag
""" await update.message.rep
y_text( 'Hello! I am a basic bot. Use /help t
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
"""Greet the use
""" user = update.effective_user.fi
async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE):
"""Roll a dic
""" result = random.randi
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
"""Show help messag
""" help_te
t = """ Available c
mmands: /start - Start
the bot /hello - Get a
reeting /roll - Rol
a dice /help - Show this
mes
def main():
app = Application.builder().toke

text
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('hello', hello))
app.add_handler(CommandHandler('roll', roll))
app.add_handler(CommandHandler('help', help_command))

print('Bot is running...')
app.run_polling()
if name == 'main':
    main()  
```


## Technical Requirements

1. **Bot registration** on platform
2. **Token authentication** with environment variables
3. **Command handlers** for all specified commands
4. **Error handling** for invalid inputs
5. **Help documentation** accessible via command

## Environment Setup

**.env file:**
```
DISCORD_TOKEN=your_discord_token_here
TELEGRAM_TOKEN=your_telegram_token_here
```


**requirements.txt:**
```
discord.py>=2.3.0
python-telegram-bot>=20.0
python-dotenv>=1.0.0
```


## Submission Requirements

Folder `BotName_YourGitHubUsername` containing:

1. `bot.py` - Bot implementation
2. `.env.example` - Token template
3. `requirements.txt` - Dependencies
4. `README.md` - Setup guide with:
   - Bot registration instructions
   - Installation steps
   - Available commands
   - Usage examples

## Resources

- [Discord.py Quickstart](https://discordpy.readthedocs.io/en/stable/quickstart.html)
- [Telegram Bot Tutorial](https://core.telegram.org/bots/tutorial)
- [Python Random Module](https://docs.python.org/3/library/random.html)


