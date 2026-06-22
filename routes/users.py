from fastapi import APIRouter

from services.user_service import create_user

from models.user import UserCreate

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
