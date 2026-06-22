from pydantic import BaseModel


class UserCreate(BaseModel):

    user_id: int

    username: str

    display_name: str | None = None

    avatar_url: str | None = None
