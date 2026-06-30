from uuid import UUID

from app.repository.user_repository import UserRepository
from app.domain.schemas.user import UserProfileResponseDTO, RegisterRequestDTO, LoginRequestDTO, TokenResponseDTO
from app.domain.models.user import User

from app.core.exceptions import NotFoundException, AlreadyExistsException, UnauthorizedException
from app.core.security import hash_password, verify_password, create_access_token

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def register(self, dto: RegisterRequestDTO) -> UserProfileResponseDTO:
        user = await self.repository.get_by_email(dto.email)

        if user is not None:
            raise AlreadyExistsException("User", dto.email)

        new_user = User(
            email=dto.email,
            password_hash=hash_password(dto.password),
            name=dto.name,
            job=dto.job
        )

        new_user = await self.repository.create(new_user)
        
        return UserProfileResponseDTO.model_validate(new_user)
    

    async def login(self, dto: LoginRequestDTO):
        user = await self.repository.get_by_email(dto.email)

        if user is None:
            raise UnauthorizedException()
        
        if not verify_password(dto.password, user.password_hash):
            raise UnauthorizedException()
        
        token = create_access_token(user.id)

        return TokenResponseDTO(
            access_token= token,
            token_type="bearer",
        )


    async def get_profile(self, id: UUID) -> UserProfileResponseDTO:
        user = await self.repository.get_by_id(id)

        if user is None:
            raise NotFoundException("User", str(id))

        return UserProfileResponseDTO.model_validate(user)