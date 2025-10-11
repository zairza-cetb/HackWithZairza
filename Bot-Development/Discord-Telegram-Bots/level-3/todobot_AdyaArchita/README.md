## Todo List Bot by AdyaArchita

I have built a user-friendly and quite efficient Telegram bot for managing personal tasks with per-user todo lists, powered by SQLite for persistent storage. This bot allows users to add, view, complete, delete, and clear tasks via simple commands, and is designed for async performance using `python-telegram-bot` and `aiosqlite`.

## Features

1.  Persistent storage: Tasks are saved in a SQLite database.
2.  Per-user isolation: Each user has their own todo list.
3.  Task management:
        * Add new tasks
        * List existing tasks
        * Mark tasks as complete
        * Delete tasks
        * Clear all tasks
4.  Task metadata: Supports priority levels and completion timestamps.
5.  Async-first architecture: Built with `asyncio` for responsive command handling.
6.  Safe and validated input: Prevents invalid task IDs and overly long tasks.
7.  Professional formatting: Uses HTML for clean task lists with strikethroughs for completed tasks.

## Commands - 
   All commands are accessed via `/todo` with optional subcommands:
         Command                  Description                                  

    /todo add [task]            Add a new task to your list.
    /todo list or /todo         Show all tasks, sorted by completion status.
    /todo complete [id]         Mark a specific task as complete.
    /todo delete [id]           Delete a task by ID.
    /todo clear                 Remove all tasks from your list.
    /todo help                  Show this help message.
    /start                      Welcome message with instructions.

## Getting Started Example
Here’s a quick walkthrough of using the bot:

1. *Add a task*                                             
```                                                 
/todo add Buy groceries                                          
```                                                         

2. *List tasks*
```
/todo list
```

3. *Complete a task*
```
/todo complete 1
```

4. *Delete a task*
```
/todo delete 2
```

5. *Clear all tasks*
```
/todo clear
```

6. *Get help*
```
/todo help
```

## Database Schema
The bot uses a *SQLite database* (`todos.sqlite`) with the following schema:
```sql
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
1. id: Auto-incremented task ID.
2. user_id: Telegram user ID for task isolation.
3. task: Text of the task (max 255 characters).
4. priority: Optional priority (default: 'medium').
5. completed: Boolean indicating completion status.
6. created_at: Timestamp when task was created.
7. completed_at: Timestamp when task was completed.

## Installation

1. *Clone the repository*:
```bash
git clone https://github.com/yourusername/todo-bot.git
cd todo-bot
```

2. *Create a virtual environment* (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

3. *Install dependencies*:
```bash
pip install -r requirements.txt
```

4. *Configure your bot token*:
Create a `.env` file in the root directory:
```env
TELEGRAM_TOKEN=YOUR_BOT_TOKEN_HERE              (Important: Keep your token secret. Do not share publicly.)
```

5. *Run the bot*:
```bash
python todo_bot.py
```
The bot will initialize the SQLite database automatically (`todos.sqlite`) and start polling Telegram.

## Dependencies
1.  [python-telegram-bot](https://pypi.org/project/python-telegram-bot/) >= 20.0
2.  [python-dotenv](https://pypi.org/project/python-dotenv/) >= 1.0.0
3.  [aiosqlite](https://pypi.org/project/aiosqlite/) >= 0.19.0

## Notes & Recommendations
1. *Data Safety*: The bot uses a *shared async database connection* for efficiency. The database file should be backed up regularly if tasks are critical.
2. *Extensibility*: New features such as *task search*, *editing tasks*, or *sorting by priority* can be added easily.
3. *Async-first*: All database operations are asynchronous, ensuring smooth performance even with multiple users.