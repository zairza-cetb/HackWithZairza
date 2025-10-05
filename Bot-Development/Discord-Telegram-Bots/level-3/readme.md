# Level 3: Database-Backed Bots

Create bots with persistent data storage using databases. Implement user data management, server settings, and stateful interactions.

## Project Options

### Option 1: Todo List Bot
Task management bot with per-user todo lists.

**Commands:**
- `/todo add [task]` - Add task
- `/todo list` - Show all tasks
- `/todo complete [id]` - Mark task complete
- `/todo delete [id]` - Delete task
- `/todo clear` - Clear all tasks

**Features:**
- SQLite database integration
- Per-user task isolation
- Task priorities and due dates
- Completion tracking
- Search and filter tasks

### Option 2: Poll Bot
Create and manage polls with voting.

**Commands:**
- `/poll create [question]` - Create poll
- `/poll options [opt1] [opt2]...` - Add options
- `/poll vote [option]` - Cast vote
- `/poll results` - Show results
- `/poll close` - Close poll

**Features:**
- Multi-option polls
- Anonymous or public voting
- Vote tracking per user
- Time-limited polls
- Results visualization

### Option 3: Server Configuration Bot
Bot for managing server settings and preferences.

**Commands:**
- `/config set [key] [value]` - Set configuration
- `/config get [key]` - Get configuration
- `/config list` - List all settings
- `/config reset [key]` - Reset to default

**Features:**
- Per-server configuration
- Role-based access control
- Configuration validation
- Backup and restore settings
- Audit logging

## Implementation Example
```
import discord
from discord.ext import commands
import sqlite3
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Database setup
def init_db():
conn = sqlite3.connect('bot_data.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS todos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
task TEXT,
completed BOOLEAN DEFAULT 0,
created_at TIMESTAMP,
completed_at TIMESTAMP
)
''')
conn.commit()
conn.close()

@bot.event
async def on_ready():
print(f'{bot.user} connected!')
init_db()

@bot.group(name='todo')
async def todo(ctx):
"""Todo list commands"""
if ctx.invoked_subcommand is None:
await ctx.send('Use: /todo [add|list|complete|delete]')

@todo.command(name='add')
async def todo_add(ctx, *, task: str):
"""Add a new task"""
conn = sqlite3.connect('bot_data.db')
c = conn.cursor()

text
c.execute(
    'INSERT INTO todos (user_id, task, created_at) VALUES (?, ?, ?)',
    (ctx.author.id, task, datetime.now())
)
conn.commit()
task_id = c.lastrowid
conn.close()

await ctx.send(f'✅ Task added! (ID: {task_id})')
@todo.command(name='list')
async def todo_list(ctx):
"""List all tasks"""
conn = sqlite3.connect('bot_data.db')
c = conn.cursor()

text
c.execute(
    'SELECT id, task, completed FROM todos WHERE user_id = ?',
    (ctx.author.id,)
)
tasks = c.fetchall()
conn.close()

if not tasks:
    await ctx.send('No tasks found!')
    return

embed = discord.Embed(
    title=f"📝 {ctx.author.name}'s Tasks",
    color=discord.Color.green()
)

for task_id, task, completed in tasks:
    status = '✅' if completed else '⬜'
    embed.add_field(
        name=f'{status} Task {task_id}',
        value=task,
        inline=False
    )

await ctx.send(embed=embed)
@todo.command(name='complete')
async def todo_complete(ctx, task_id: int):
"""Mark a task as complete"""
conn = sqlite3.connect('bot_data.db')
c = conn.cursor()

text
c.execute(
    '''UPDATE todos SET completed = 1, completed_at = ?
       WHERE id = ? AND user_id = ?''',
    (datetime.now(), task_id, ctx.author.id)
)

if c.rowcount > 0:
    await ctx.send(f'✅ Task {task_id} completed!')
else:
    await ctx.send('Task not found!')

conn.commit()
conn.close()
@todo.command(name='delete')
async def todo_delete(ctx, task_id: int):
"""Delete a task"""
conn = sqlite3.connect('bot_data.db')
c = conn.cursor()

text
c.execute(
    'DELETE FROM todos WHERE id = ? AND user_id = ?',
    (task_id, ctx.author.id)
)

if c.rowcount > 0:
    await ctx.send(f'🗑️ Task {task_id} deleted!')
else:
    await ctx.send('Task not found!')

conn.commit()
conn.close()
bot.run(TOKEN)
```


## Database Schema Examples

**SQLite Schema (todos):**
```
CREATE TABLE todos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER NOT NULL,
task TEXT NOT NULL,
priority TEXT DEFAULT 'medium',
completed BOOLEAN DEFAULT 0,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
completed_at TIMESTAMP
);

CREATE INDEX idx_user_id ON todos(user_id);
```


## Technical Requirements

1. **Database connection** with proper initialization
2. **CRUD operations** for data management
3. **Data validation** before storage
4. **Transaction handling** for data integrity
5. **Indexed queries** for performance
6. **Database migration** support

## Dependencies
```
discord.py>=2.3.0
python-telegram-bot>=20.0
python-dotenv>=1.0.0
aiosqlite>=0.19.0
```


## Submission Requirements

Folder `BotName_YourGitHubUsername` containing:

1. `bot.py` - Bot implementation
2. `database.py` - Database utilities
3. `schema.sql` - Database schema
4. `.env.example` - Configuration template
5. `requirements.txt` - Dependencies
6. `README.md` - Documentation with:
   - Database setup instructions
   - Command documentation
   - Data model explanation

## Resources

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Python SQLite3](https://docs.python.org/3/library/sqlite3.html)
- [Discord.py Command Groups](https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html#groups)

