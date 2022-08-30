from re import L
from fastapi import APIRouter, Depends
from app.user.repositories.user import UserRepository
from app.user.entities.schemas.user import UserCreate

router = APIRouter()


@router.post("")
async def create_user(user: UserCreate, user_repository: UserRepository = Depends(UserRepository)):
    print(user.id)
    return user_repository.create(user)


@router.get("/{user_id}")
async def read_user(user_id: str, user_repository: UserRepository = Depends(UserRepository)):
    return user_repository.read(user_id)
