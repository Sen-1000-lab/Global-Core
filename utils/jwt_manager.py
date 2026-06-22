from jose import jwt
from datetime import datetime
from datetime import timedelta

from config import (
    JWT_SECRET,
    JWT_ALGORITHM
)


def create_token(
    user_id: int
):

    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow()
        + timedelta(days=30)
    }

    return jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )


def verify_token(
    token: str
):

    return jwt.decode(
        token,
        JWT_SECRET,
        algorithms=[
            JWT_ALGORITHM
        ]
    )
