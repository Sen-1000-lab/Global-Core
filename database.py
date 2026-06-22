import asyncpg

from config import DATABASE_URL

pool = None


async def connect_db():
    global pool

    pool = await asyncpg.create_pool(
        DATABASE_URL,
        min_size=1,
        max_size=20
    )


async def get_pool():
    return pool
