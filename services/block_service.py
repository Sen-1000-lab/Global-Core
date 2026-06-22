from database import pool

async def add_block(
user_id: int,
blocked_user_id: int
):

```
async with pool.acquire() as conn:

    await conn.execute(
        """
        INSERT INTO blocks
        (
            user_id,
            blocked_user_id
        )
        VALUES
        (
            $1,
            $2
        )
        """,
        user_id,
        blocked_user_id
    )
```

async def remove_block(
user_id: int,
blocked_user_id: int
):

```
async with pool.acquire() as conn:

    await conn.execute(
        """
        DELETE FROM blocks
        WHERE
            user_id = $1
            AND
            blocked_user_id = $2
        """,
        user_id,
        blocked_user_id
    )
```

async def get_blocks(
user_id: int
):

```
async with pool.acquire() as conn:

    return await conn.fetch(
        """
        SELECT *
        FROM blocks
        WHERE user_id = $1
        """,
        user_id
    )
```
