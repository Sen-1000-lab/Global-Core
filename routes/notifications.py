from fastapi import APIRouter

from services.notification_service import (
send_notification,
get_notifications,
mark_as_read
)

router = APIRouter()

@router.post("/send")
async def send_notification_route(
user_id: int,
title: str,
content: str
):

```
await send_notification(
    user_id,
    title,
    content
)

return {
    "success": True
}
```

@router.get("/list/{user_id}")
async def get_notification_list(
user_id: int
):

```
notifications = await get_notifications(
    user_id
)

return {
    "success": True,
    "notifications": [
        dict(x)
        for x in notifications
    ]
}
```

@router.patch("/read/{notification_id}")
async def read_notification(
notification_id: int
):

```
await mark_as_read(
    notification_id
)

return {
    "success": True
}
```
