from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )
 
    APP_NAME: str = "Mobile apps Lab4 - Auth"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Basic auth App for Lab4"

    API_V1_PREFIX: str = "/api/v1"
 
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:8080"]
 
    DATABASE_URL: str
 
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
 
 
settings = Settings()
