from database import pool

async def add_friend(
user_id: int,
friend_id: int
):

```
async with pool.acquire() as conn:

    await conn.execute(
        """
        INSERT INTO friends
        (
            user_id,
            friend_id
        )
        VALUES
        (
            $1,
            $2
        )
        """,
        user_id,
        friend_id
    )
```

async def remove_friend(
user_id: int,
friend_id: int
):

```
async with pool.acquire() as conn:

    await conn.execute(
        """
        DELETE FROM friends
        WHERE
            user_id = $1
            AND
            friend_id = $2
        """,
        user_id,
        friend_id
    )
```

async def get_friends(
user_id: int
):

```
async with pool.acquire() as conn:

    return await conn.fetch(
        """
        SELECT *
        FROM friends
        WHERE user_id = $1
        """,
        user_id
    )
```
