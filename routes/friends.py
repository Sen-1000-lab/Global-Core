from fastapi import APIRouter

from services.friend_service import (
add_friend,
remove_friend,
get_friends
)

router = APIRouter()

@router.post("/add")
async def add_friend_route(
user_id: int,
friend_id: int
):

```
await add_friend(
    user_id,
    friend_id
)

return {
    "success": True
}
```

@router.delete("/remove")
async def remove_friend_route(
user_id: int,
friend_id: int
):

```
await remove_friend(
    user_id,
    friend_id
)

return {
    "success": True
}
```

@router.get("/list/{user_id}")
async def get_friend_list(
user_id: int
):

```
friends = await get_friends(
    user_id
)

return {
    "success": True,
    "friends": [
        dict(x)
        for x in friends
    ]
}
```
