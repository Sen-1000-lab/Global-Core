from fastapi import APIRouter

from services.favorite_service import (
add_favorite,
remove_favorite,
get_favorites
)

router = APIRouter()

@router.post("/add")
async def add_favorite_route(
user_id: int,
target_user_id: int
):

```
await add_favorite(
    user_id,
    target_user_id
)

return {
    "success": True
}
```

@router.delete("/remove")
async def remove_favorite_route(
user_id: int,
target_user_id: int
):

```
await remove_favorite(
    user_id,
    target_user_id
)

return {
    "success": True
}
```

@router.get("/list/{user_id}")
async def get_favorite_list(
user_id: int
):

```
favorites = await get_favorites(
    user_id
)

return {
    "success": True,
    "favorites": [
        dict(x)
        for x in favorites
    ]
}
```
