from jose import jwt
from jose import JWTError

from datetime import datetime
from datetime import timedelta

from config import (
JWT_SECRET,
JWT_ALGORITHM
)

def create_token(
user_id: int
):

```
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
```

def verify_token(
token: str
):

```
try:

    payload = jwt.decode(
        token,
        JWT_SECRET,
        algorithms=[
            JWT_ALGORITHM
        ]
    )

    return payload

except JWTError:

    return None
```
