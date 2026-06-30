from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field

class RegisterRequestDTO(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)
    name: str = Field(..., min_length=1, max_length=100)
    job: str | None = Field(default=None, max_length=100)

class LoginRequestDTO(BaseModel):
    email: EmailStr
    password: str

class UserProfileResponseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    email: EmailStr
    name: str
    job: str | None
    provider: str
    created_at: datetime

class TokenResponseDTO(BaseModel):
    access_token: str
    token_type: str = "bearer"