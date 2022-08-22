import uvicorn

from fastapi import FastAPI

from app.common.config import API_V1
from app.user.routers import users

app = FastAPI(title='FastAPI TODO', docs_url=f'{API_V1}/docs')

app.include_router(users.router, prefix=f'{API_V1}/users', tags=['users'])


if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)