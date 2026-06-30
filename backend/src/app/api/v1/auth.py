from fastapi import APIRouter, Depends, HTTPException

from app.domain.schemas.user import (
    UserProfileResponseDTO,
    LoginRequestDTO,
    RegisterRequestDTO,
    TokenResponseDTO
)
from app.service.user_service import UserService
from app.api.deps import get_user_service

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", status_code=201)
async def register(
    dto: RegisterRequestDTO,
    service: UserService = Depends(get_user_service) 
):
    return await service.register(dto)
    
@router.post("/login", response_model=TokenResponseDTO, status_code=200)
async def login(
    dto: LoginRequestDTO,
    service: UserService = Depends(get_user_service) 
):
    return await service.login(dto)

@router.get("/profile", response_model=UserProfileResponseDTO, status_code=200)
async def get_profile(
    user: CurrentUser,
    service: UserService = Depends(get_user_service) 
):
    return await service.get_profile()