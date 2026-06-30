from fastapi import APIRouter, Depends

from app.domain.schemas.user import (
    UserProfileResponseDTO,
    LoginRequestDTO,
    RegisterRequestDTO,
)
from app.service.user_service import UserService
from app.api.deps import get_user_service

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/register", status_code=201)
async def register(
    dto: RegisterRequestDTO,
    service: UserService = Depends(get_user_service) 
):
    return
    
@router.post("/login", status_code=200)
async def login(
    dto: LoginRequestDTO,
    service: UserService = Depends(get_user_service) 
):
    return

@router.get("/profile", response_model=UserProfileResponseDTO, status_code=200)
async def get_profile(
    service: UserService = Depends(get_user_service) 
):
    return