import asyncio
import uvicorn

from threading import Thread

from api.app import app

from database import connect_db


async def startup():

    await connect_db()


def start_api():

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )


async def main():

    await startup()

    Thread(
        target=start_api,
        daemon=True
    ).start()

    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
