from typing import Dict, List, Type, Tuple

from app.common.exceptions import EntityNotFoundException
from app.common.repository.base_repository import BaseRepository, M


class MemoryRepository(BaseRepository[M]):
    Entity: Type[M]
    memory_repository: Dict

    def __len__(self):
        pass

    def create(self, entity: M) -> M:
        self.memory_repository[entity.id] = entity.dict()
        return self.memory_repository[entity.id]

    def read(self, id: str) -> M:
        if id not in self.memory_repository:
            raise EntityNotFoundException(id, self.Entity)
        return self.Entity(**self.memory_repository[id])

    def query(self, limit: int = 20, offset: int = 0) -> List[M]:
        queryset = self.memory_repository.values()
        return [self.Entity(**entity) for entity in queryset], len(queryset)

    def update(self, id: str, entity: M) -> M:
        if id not in self.memory_repository:
            raise EntityNotFoundException(id, self.Entity)
        self.memory_repository[id] = M.dict()
        return self.memory_repository[id]

    def delete(self, id: str) -> None:
        if id not in self.memory_repository:
            raise EntityNotFoundException(id, self.Entity)
        del self.memory_repository[id]
