from fastapi import FastAPI

from routes.users import router as user_router
from routes.friends import router as friend_router
from routes.blocks import router as block_router
from routes.favorites import router as favorite_router

app = FastAPI(
title="Globally Core API"
)

app.include_router(
user_router,
prefix="/api/users",
tags=["Users"]
)

app.include_router(
friend_router,
prefix="/api/friends",
tags=["Friends"]
)

app.include_router(
block_router,
prefix="/api/blocks",
tags=["Blocks"]
)

app.include_router(
favorite_router,
prefix="/api/favorites",
tags=["Favorites"]
)

@app.get("/")
async def root():

```
return {
    "success": True,
    "service": "Globally Core"
}
```

@app.get("/health")
async def health():

```
return {
    "status": "ok"
}
```
