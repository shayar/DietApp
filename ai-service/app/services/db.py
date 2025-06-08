import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_DB_URL = os.getenv("SUPABASE_DB_URL")

class Database:
    pool: asyncpg.Pool = None

    @classmethod
    async def connect(cls):
        if cls.pool is None:
            cls.pool = await asyncpg.create_pool(SUPABASE_DB_URL)

    @classmethod
    async def close(cls):
        if cls.pool:
            await cls.pool.close()
            cls.pool = None

db = Database()
