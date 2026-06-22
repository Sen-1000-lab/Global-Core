from fastapi import FastAPI

from routes.users import router as user_router

app = FastAPI(
    title="Globally Core API"
)

app.include_router(
    user_router,
    prefix="/api/users",
    tags=["Users"]
)


@app.get("/")
async def root():

    return {
        "success": True,
        "service": "Globally Core"
    }


@app.get("/health")
async def health():

    return {
        "status": "ok"
    }
