from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.domain.schemas.user import (
    UserProfileResponseDTO,
    LoginRequestDTO,
    RegisterRequestDTO,
    TokenResponseDTO
)
from app.service.user_service import UserService
from app.api.deps import get_user_service
from app.core.security import CurrentUser

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", status_code=201)
async def register(
    dto: RegisterRequestDTO,
    service: UserService = Depends(get_user_service)
):
    return await service.register(dto)

@router.post("/login", response_model=TokenResponseDTO, status_code=200)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: UserService = Depends(get_user_service)
):
    dto = LoginRequestDTO(email=form_data.username, password=form_data.password)
    return await service.login(dto)

@router.get("/profile", response_model=UserProfileResponseDTO, status_code=200)
async def get_profile(
    user: CurrentUser,
    service: UserService = Depends(get_user_service)
):
    return await service.get_profile(user.id)