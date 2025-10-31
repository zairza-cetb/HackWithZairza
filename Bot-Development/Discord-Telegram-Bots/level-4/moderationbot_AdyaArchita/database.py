import aiosqlite

class Database:
    def __init__(self, db_name="moderation.db"):
        self.db_name = db_name

    async def init_db(self):
        """Initializes the database and creates tables if they don't exist."""
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS warnings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    chat_id INTEGER NOT NULL,
                    moderator_id INTEGER NOT NULL,
                    reason TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            await db.commit()
        print("Database initialized successfully.")

    async def add_warning(self, user_id, chat_id, moderator_id, reason):
        """Adds a warning and returns the new warning's ID and the user's total warning count."""
        async with aiosqlite.connect(self.db_name) as db:
            cursor = await db.execute(
                "INSERT INTO warnings (user_id, chat_id, moderator_id, reason) VALUES (?, ?, ?, ?)",
                (user_id, chat_id, moderator_id, reason)
            )
            await db.commit()
            new_warning_id = cursor.lastrowid

            cursor = await db.execute(
                "SELECT COUNT(id) FROM warnings WHERE user_id = ? AND chat_id = ?",
                (user_id, chat_id)
            )
            total_warnings = await cursor.fetchone()
            return new_warning_id, total_warnings[0] if total_warnings else 0

    async def get_warnings(self, user_id, chat_id):
        """Retrieves all warnings for a specific user in a chat."""
        async with aiosqlite.connect(self.db_name) as db:
            # This query now selects all columns to match the handler's expectation.
            cursor = await db.execute(
                "SELECT id, user_id, chat_id, moderator_id, reason, timestamp FROM warnings WHERE user_id = ? AND chat_id = ?",
                (user_id, chat_id)
            )
            rows = await cursor.fetchall()
            return rows

    async def remove_warning(self, warning_id: int) -> bool:
        """Removes a warning by its unique ID."""
        async with aiosqlite.connect(self.db_name) as db:
            cursor = await db.execute("DELETE FROM warnings WHERE id = ?", (warning_id,))
            await db.commit()
            # The cursor.rowcount will be 1 if a row was deleted, and 0 otherwise.
            return cursor.rowcount > 0

