from database import pool

async def add_favorite(
user_id: int,
target_user_id: int
):

```
async with pool.acquire() as conn:

    await conn.execute(
        """
        INSERT INTO favorites
        (
            user_id,
            target_user_id
        )
        VALUES
        (
            $1,
            $2
        )
        """,
        user_id,
        target_user_id
    )
```

async def remove_favorite(
user_id: int,
target_user_id: int
):

```
async with pool.acquire() as conn:

    await conn.execute(
        """
        DELETE FROM favorites
        WHERE
            user_id = $1
            AND
            target_user_id = $2
        """,
        user_id,
        target_user_id
    )
```

async def get_favorites(
user_id: int
):

```
async with pool.acquire() as conn:

    return await conn.fetch(
        """
        SELECT *
        FROM favorites
        WHERE user_id = $1
        """,
        user_id
    )
```
