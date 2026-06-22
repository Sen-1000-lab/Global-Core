from fastapi import APIRouter

from services.block_service import (
add_block,
remove_block,
get_blocks
)

router = APIRouter()

@router.post("/add")
async def add_block_route(
user_id: int,
blocked_user_id: int
):

```
await add_block(
    user_id,
    blocked_user_id
)

return {
    "success": True
}
```

@router.delete("/remove")
async def remove_block_route(
user_id: int,
blocked_user_id: int
):

```
await remove_block(
    user_id,
    blocked_user_id
)

return {
    "success": True
}
```

@router.get("/list/{user_id}")
async def get_block_list(
user_id: int
):

```
blocks = await get_blocks(
    user_id
)

return {
    "success": True,
    "blocks": [
        dict(x)
        for x in blocks
    ]
}
```
