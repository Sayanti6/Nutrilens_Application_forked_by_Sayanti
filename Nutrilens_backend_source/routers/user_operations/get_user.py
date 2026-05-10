from fastapi import APIRouter, Depends
from typing import Annotated
from Nutrilens_backend_source.auth import get_current_active_user
from Nutrilens_backend_source.schemas import User

router = APIRouter()

@router.get("/users/me/")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> User:
    return current_user