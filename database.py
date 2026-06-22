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


async def create_tables():

    async with pool.acquire() as conn:

        await conn.execute("""

        CREATE TABLE IF NOT EXISTS users (

            user_id BIGINT PRIMARY KEY,

            username TEXT,

            display_name TEXT,

            avatar_url TEXT,

            trust_score INTEGER DEFAULT 50,

            xp BIGINT DEFAULT 0,

            level INTEGER DEFAULT 1,

            coins BIGINT DEFAULT 0,

            bank BIGINT DEFAULT 0,

            job TEXT DEFAULT 'none',

            bio VARCHAR(50),

            created_at TIMESTAMP DEFAULT NOW(),

            updated_at TIMESTAMP DEFAULT NOW()

        )

        """)

        await conn.execute("""

        CREATE TABLE IF NOT EXISTS friends (

            id SERIAL PRIMARY KEY,

            user_id BIGINT,

            friend_id BIGINT,

            created_at TIMESTAMP DEFAULT NOW()

        )

        """)

        await conn.execute("""

        CREATE TABLE IF NOT EXISTS blocks (

            id SERIAL PRIMARY KEY,

            user_id BIGINT,

            blocked_user_id BIGINT,

            created_at TIMESTAMP DEFAULT NOW()

        )

        """)
