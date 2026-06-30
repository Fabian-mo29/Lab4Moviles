from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.models import user
class UserRepository(ABC):
    @abstractmethod
    async def get_by_id(id: UUID) -> user:
        pass