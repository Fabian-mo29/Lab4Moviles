from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.settings import settings
from app.api.v1 import api_router
from app.core.database import Base, engine

from fastapi.responses import JSONResponse

from app.core.exception_handlers import register_exception_handlers

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


    yield
    print("Shutting down...")


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description=settings.APP_DESCRIPTION,
        lifespan=lifespan,
    )
 
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
 
    app.include_router(api_router, prefix=settings.API_V1_PREFIX)
 
    return app
 
 
app = create_app()

register_exception_handlers(app)

@app.get("/health")
async def health():
    return { "status": "Healthy" }
