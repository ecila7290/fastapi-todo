from app.common.repository.memory_repository import MemoryRepository
from app.user.entities.schemas.user import UserBase

M = UserBase
UserDictionary = {}


class UserRepository(MemoryRepository[M]):
    Entity = M
    memory_repository = UserDictionary
