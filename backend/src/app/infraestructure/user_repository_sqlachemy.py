from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.repository.user_repository import  UserRepository

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, db: AsyncSession):
        self.db = db