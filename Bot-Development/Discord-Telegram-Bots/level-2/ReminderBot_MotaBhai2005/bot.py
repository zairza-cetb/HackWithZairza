import discord
from discord.ext import commands, tasks
from datetime import timedelta, datetime
import asyncio
import pytz
import os
from dotenv import load_dotenv
from zoneinfo import ZoneInfo, available_timezones
import sys

if sys.platform.startswith('win'):
    import tzdata

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

reminders = []
user_timezone = {}

@bot.event
async def on_ready():
    print(f'✅ {bot.user} is online!')
    check_reminders.start()

@bot.command(name='settimezone')
async def set_timezone(ctx, tz: str):
    """Set your timezone, e.g. /settimezone Asia/Kolkata"""
    try:
        ZoneInfo(tz)  # Validate
        user_timezone[ctx.author.id] = tz
        await ctx.send(f"🌍 Timezone set to **{tz}**")
    except Exception:
        await ctx.send("❌ Invalid timezone! Try formats like `Asia/Kolkata` or `America/New_York`")

@bot.command(name='remind')
async def remind(ctx, time: str, *, message: str):
    """
    Set a reminder.
    Examples:
    /remind 10m Take a break
    /remind 2h Submit report
    /remind 1d Buy groceries
    """

    try:
        units = {'m': 60, 'h': 3600, 'd': 86400}
        unit = time[-1]
        value = int(time[:-1])

        if unit not in units:
            await ctx.send("⏳ Use 'm', 'h', or 'd' (e.g. 10m, 2h, 1d)")
            return
        seconds = value * units[unit]

    except ValueError:
        await ctx.send("⚠️ Invalid time format. Try `/remind 10m Drink water`")
        return

    # Get user timezone or default to UTC
    tz_name = user_timezone.get(ctx.author.id, "UTC")
    user_tz = ZoneInfo(tz_name)

    # Time in user's timezone
    now_local = datetime.now(user_tz)
    reminder_time_local = now_local + timedelta(seconds=seconds)

    # Convert to UTC for consistency
    reminder_time_utc = reminder_time_local.astimezone(ZoneInfo("UTC"))

    reminders.append({
        'user': ctx.author.id,
        'channel': ctx.channel.id,
        'time': reminder_time_utc,
        'message': message,
        'tz': tz_name
    })

    await ctx.send(f"✅ Reminder set for **{value}{unit}** from now ({tz_name})")

@bot.command(name='reminders')
async def list_reminders(ctx):
    """List your active reminders"""
    user_reminders = [
        (i, r) for i, r in enumerate(reminders) if r['user'] == ctx.author.id
    ]
    if not user_reminders:
        await ctx.send('No Active Reminder!')
        return
    
    desc = ""
    now_utc = datetime.now(ZoneInfo("UTC"))
    
    for i, r in user_reminders:
        time_left = r['time'] - now_utc
        minutes = int(time_left.total_seconds() // 60)
        user_tz = ZoneInfo(r['tz'])
        local_time = r['time'].astimezone(user_tz)
        desc += f"**ID {i}** - {r['message']}\n⏰ in {minutes} min (at {local_time.strftime('%I:%M %p')})\n"

    embed = discord.Embed(
        title = f"{ctx.author.display_name}'s Active Reminders",
        description=desc,
        color=discord.Color.green()  
    )
    await ctx.send(embed=embed)

@bot.command(name='cancel')
async def cancel_reminder(ctx, reminder_id: int):
    """Cancel a reminder by its ID (check with /reminders)"""
    if reminder_id < 0 or reminder_id >= len(reminders):
        await ctx.send("❌ Invalid reminder ID.")
        return
    reminder = reminders[reminder_id]
    if reminder['user'] != ctx.author.id:
        await ctx.send('🚫 You can only cancel your own reminders!')
        return
    
    reminders.pop(reminder_id)
    await ctx.send(f'🗑 Reminder #{reminder_id} cancelled!')

@tasks.loop(seconds=30)
async def check_reminders():
    """Check and send reminders"""
    now_utc = datetime.now(ZoneInfo("UTC"))
    due = [r for r in reminders if r['time'] <= now_utc]

    for r in due:
        try:
            channel = bot.get_channel(r['channel'])
            user = await bot.fetch_user(r['user'])
            if channel and user:
                local_time = r['time'].astimezone(ZoneInfo(r['tz']))
                await channel.send(
                    f'🔔 {user.mention}, Reminder: **{r["message"]}** '
                    f'(scheduled for {local_time.strftime("%I:%M %p")})'
                )
            reminders.remove(r)
        except Exception as e:
            print(f"Error processing reminder: {e}")
            reminders.remove(r)

bot.run(DISCORD_TOKEN)