# Level 4: Advanced Bots

Build production-ready bots with advanced features including moderation tools, audio processing, interactive games, and comprehensive logging systems.

## Project Options

### Option 1: Moderation Bot
Comprehensive server moderation with auto-moderation features.

**Commands:**
- `/warn [user] [reason]` - Warn user
- `/kick [user] [reason]` - Kick user
- `/ban [user] [duration] [reason]` - Ban user
- `/mute [user] [duration]` - Mute user
- `/unmute [user]` - Unmute user
- `/warnings [user]` - View warnings
- `/clean [amount]` - Delete messages

**Features:**
- Auto-moderation (spam, profanity)
- Warning system with escalation
- Temporary bans and mutes
- Logging all mod actions
- Permission-based commands
- Configurable auto-mod rules

### Option 2: Music Bot
Audio playback bot with queue management.

**Commands:**
- `/play [song]` - Play song
- `/pause` - Pause playback
- `/resume` - Resume playback
- `/skip` - Skip current song
- `/queue` - Show queue
- `/volume [level]` - Set volume
- `/leave` - Leave voice channel

**Features:**
- YouTube/Spotify integration
- Queue management
- Playlist support
- Audio streaming
- Volume control
- Now playing display

### Option 3: Interactive Game Bot
Bot with multiple interactive games.

**Commands:**
- `/trivia start` - Start trivia game
- `/tictactoe [user]` - Play tic-tac-toe
- `/hangman` - Start hangman
- `/leaderboard` - Show scores

**Features:**
- Multiple game types
- Turn-based gameplay
- Score tracking
- Leaderboards
- Timed responses
- Interactive buttons/reactions

## Implementation Example
```
import discord
from discord.ext import commands
import logging
from datetime import datetime, timedelta
import json
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

Setup logging
logging.basicConfig(
level=logging.INFO,
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
handlers=[
logging.FileHandler('bot.log'),
logging.StreamHandler()
]
)
logger = logging.getLogger('bot')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

Load configuration
with open('config.json', 'r') as f:
config = json.load(f)

@bot.event
async def on_ready():
logger.info(f'{bot.user} is ready!')
await bot.change_presence(
activity=discord.Game(name="Moderating server")
)

@bot.event
async def on_message(message):
if message.author.bot:
return

text
# Auto-moderation
if any(word in message.content.lower() for word in config['banned_words']):
    await message.delete()
    await message.channel.send(
        f'{message.author.mention} Please watch your language!',
        delete_after=5
    )
    logger.warning(f'Deleted message from {message.author}: {message.content}')
    return

await bot.process_commands(message)
@bot.command(name='warn')
@commands.has_permissions(kick_members=True)
async def warn_user(ctx, member: discord.Member, *, reason: str):
"""Warn a user"""
# Save warning to database
logger.info(f'{ctx.author} warned {member} for: {reason}')

text
embed = discord.Embed(
    title='⚠️ User Warned',
    color=discord.Color.orange()
)
embed.add_field(name='User', value=member.mention)
embed.add_field(name='Moderator', value=ctx.author.mention)
embed.add_field(name='Reason', value=reason, inline=False)
embed.timestamp = datetime.now()

await ctx.send(embed=embed)

# DM user
try:
    await member.send(f'You have been warned in {ctx.guild.name} for: {reason}')
except:
    pass
@bot.command(name='kick')
@commands.has_permissions(kick_members=True)
async def kick_user(ctx, member: discord.Member, *, reason: str = 'No reason provided'):
"""Kick a user from the server"""
await member.kick(reason=reason)
logger.info(f'{ctx.author} kicked {member} for: {reason}')

text
embed = discord.Embed(
    title='👢 User Kicked',
    color=discord.Color.red()
)
embed.add_field(name='User', value=f'{member.name}#{member.discriminator}')
embed.add_field(name='Moderator', value=ctx.author.mention)
embed.add_field(name='Reason', value=reason, inline=False)

await ctx.send(embed=embed)
@bot.command(name='clean')
@commands.has_permissions(manage_messages=True)
async def clean_messages(ctx, amount: int):
"""Delete messages in channel"""
if amount > 100:
await ctx.send('Cannot delete more than 100 messages at once!')
return

text
deleted = await ctx.channel.purge(limit=amount + 1)
logger.info(f'{ctx.author} cleaned {len(deleted)-1} messages')

msg = await ctx.send(f'🗑️ Deleted {len(deleted)-1} messages!')
await msg.delete(delay=5)
@bot.command(name='serverinfo')
async def server_info(ctx):
"""Display server information"""
guild = ctx.guild

text
embed = discord.Embed(
    title=f'{guild.name} Server Info',
    color=discord.Color.blue()
)
embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
embed.add_field(name='Owner', value=guild.owner.mention)
embed.add_field(name='Members', value=guild.member_count)
embed.add_field(name='Roles', value=len(guild.roles))
embed.add_field(name='Created', value=guild.created_at.strftime('%Y-%m-%d'))

await ctx.send(embed=embed)
@bot.event
async def on_command_error(ctx, error):
"""Global error handler"""
if isinstance(error, commands.MissingPermissions):
await ctx.send('❌ You do not have permission to use this command!')
elif isinstance(error, commands.MissingRequiredArgument):
await ctx.send(f'❌ Missing argument: {error.param.name}')
else:
logger.error(f'Error: {error}')
await ctx.send('❌ An error occurred!')

bot.run(TOKEN)
```

## Configuration Example

**config.json:**
```
{
"prefix": "/",
"mod_log_channel": 123456789,
"banned_words": ["word1", "word2"],
"auto_mod": {
"spam_threshold": 5,
"spam_interval": 5,
"max_mentions": 5
},
"roles": {
"moderator": 123456789,
"admin": 987654321
}
}
```


## Technical Requirements

1. **Permission system** with role checks
2. **Comprehensive logging** to file and console
3. **Error handling** for all commands
4. **Configuration management** via files
5. **Async operations** for all I/O
6. **Database integration** for persistent data
7. **Event listeners** for moderation
8. **Embed messages** for professional output

## Dependencies
```
discord.py>=2.3.0
python-telegram-bot>=20.0
yt-dlp>=2023.10.0
PyNaCl>=1.5.0
python-dotenv>=1.0.0
aiosqlite>=0.19.0
```


## Submission Requirements

Folder `BotName_YourGitHubUsername` containing:

1. `bot.py` - Main bot file
2. `cogs/` - Command categories (optional)
3. `config.json.example` - Configuration template
4. `database.py` - Database utilities
5. `.env.example` - Token template
6. `requirements.txt` - Dependencies
7. `README.md` - Complete documentation
8. `DEPLOYMENT.md` - Production deployment guide

## Advanced Features

- Command cooldowns and rate limiting
- Custom permission decorators
- Cog-based command organization
- Auto-backup systems
- Health monitoring
- Graceful shutdown handling

## Resources

- [Discord.py Cogs](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html)
- [Discord Permissions](https://discord.com/developers/docs/topics/permissions)
- [Python Logging](https://docs.python.org/3/library/logging.html)
- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)
