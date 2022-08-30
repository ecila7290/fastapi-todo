import datetime
import uuid

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr | None = None
    created_at: datetime.datetime | None = None
    last_updated_at: datetime.datetime | None = None
    is_active: bool | None = True
    is_superuser: bool = False
    username: str | None = None


class UserCreate(UserBase):
    id: str = str(uuid.uuid4())
    email: EmailStr
    password: str
    username: str
    created_at: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)


class UserUpdate(UserBase):
    username: str | None = None
    password: str | None = None
    last_updated_at: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)
