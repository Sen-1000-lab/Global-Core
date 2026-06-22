from fastapi import FastAPI

app = FastAPI(
    title="Globally Core API"
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
