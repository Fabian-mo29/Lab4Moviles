from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.models import User
class UserRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: UUID) -> User:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> User:
        pass
    
    @abstractmethod
    async def create(self, user: User) -> User:
        pass