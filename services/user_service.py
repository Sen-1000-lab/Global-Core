from database import pool


async def create_user(
    user_id,
    username,
    display_name,
    avatar_url
):

    async with pool.acquire() as conn:

        await conn.execute(
            """
            INSERT INTO users
            (
                user_id,
                username,
                display_name,
                avatar_url
            )

            VALUES
            (
                $1,
                $2,
                $3,
                $4
            )

            ON CONFLICT (user_id)
            DO NOTHING
            """,

            user_id,
            username,
            display_name,
            avatar_url
        )


async def get_user(
    user_id: int
):

    async with pool.acquire() as conn:

        return await conn.fetchrow(
            """
            SELECT *
            FROM users
            WHERE user_id = $1
            """,
            user_id
        )
