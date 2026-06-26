from database import pool

async def send_notification(
user_id: int,
title: str,
content: str
):

```
async with pool.acquire() as conn:

    await conn.execute(
        """
        INSERT INTO notifications
        (
            user_id,
            title,
            content
        )
        VALUES
        (
            $1,
            $2,
            $3
        )
        """,
        user_id,
        title,
        content
    )
```

async def get_notifications(
user_id: int
):

```
async with pool.acquire() as conn:

    return await conn.fetch(
        """
        SELECT *
        FROM notifications
        WHERE user_id = $1
        ORDER BY created_at DESC
        LIMIT 100
        """,
        user_id
    )
```

async def mark_as_read(
notification_id: int
):

```
async with pool.acquire() as conn:

    await conn.execute(
        """
        UPDATE notifications
        SET read = TRUE
        WHERE id = $1
        """,
        notification_id
    )
```
