from re import L
from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def get_user():
    return {'id':1, 'username':'foo'}