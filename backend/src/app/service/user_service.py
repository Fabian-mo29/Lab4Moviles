from uuid import UUID

from app.repository.user_repository import UserRepository
from app.domain.schemas.user import UserProfileResponseDTO, RegisterRequestDTO, LoginRequestDTO

from app.core.exceptions import NotFoundException
class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def register(self, dto: RegisterRequestDTO):
        return
    

    async def log_in(self, dto: LoginRequestDTO):
        return


    async def get_profile(self, id: UUID) -> UserProfileResponseDTO:
        user = await self.repository.get_by_id(id)

        if user is None:
            raise NotFoundException("User", str(id))

        return UserProfileResponseDTO.model_validate(user)