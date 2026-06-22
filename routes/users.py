from fastapi import APIRouter

from models.user import UserCreate

from services.user_service import (
    create_user,
    get_user
)

router = APIRouter()


@router.post("/create")
async def create_user_route(
    data: UserCreate
):

    await create_user(
        data.user_id,
        data.username,
        data.display_name,
        data.avatar_url
    )

    return {
        "success": True
    }


@router.get("/{user_id}")
async def get_user_route(
    user_id: int
):

    user = await get_user(
        user_id
    )

    if not user:

        return {
            "success": False
        }

    return {
        "success": True,
        "data": dict(user)
    }
