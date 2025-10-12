import aiosqlite
import logging

DB_FILE = "todos.sqlite"
logger = logging.getLogger(__name__)

async def init_db():
    async with aiosqlite.connect(DB_FILE) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                task TEXT NOT NULL,
                priority TEXT DEFAULT 'medium',
                completed BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP
            );
        """)
        await db.execute(""" CREATE INDEX IF NOT EXISTS idx_user_id ON todos(user_id); """)
        await db.commit()
        logger.info("Database tables and indexes are set up.")

async def add_task(user_id: int, task: str, priority: str = 'medium'):
    async with aiosqlite.connect(DB_FILE) as db:
        await db.execute(
            "INSERT INTO todos (user_id, task, priority) VALUES (?, ?, ?)",
            (user_id, task, priority)
        )
        await db.commit()

async def get_tasks(user_id: int):
    async with aiosqlite.connect(DB_FILE) as db:
        async with db.execute(
            "SELECT id, task, completed FROM todos WHERE user_id = ? ORDER BY completed ASC, created_at DESC",
            (user_id,)
        ) as cursor:
            return await cursor.fetchall()

async def update_task_status(task_id: int, user_id: int, completed: bool):
    async with aiosqlite.connect(DB_FILE) as db:
        completed_at_sql = "CURRENT_TIMESTAMP" if completed else "NULL"
        cursor = await db.execute(
            f"""
            UPDATE todos 
            SET completed = ?, completed_at = {completed_at_sql}
            WHERE id = ? AND user_id = ?
            """,
            (completed, task_id, user_id)
        )
        await db.commit()
        return cursor.rowcount

async def delete_task(task_id: int, user_id: int):
    async with aiosqlite.connect(DB_FILE) as db:
        cursor = await db.execute(
            "DELETE FROM todos WHERE id = ? AND user_id = ?",
            (task_id, user_id)
        )
        await db.commit()
        return cursor.rowcount

async def clear_tasks(user_id: int):
    async with aiosqlite.connect(DB_FILE) as db:
        await db.execute("DELETE FROM todos WHERE user_id = ?", (user_id,))
        await db.commit()
