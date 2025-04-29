from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.settings import settings
from app.router.users import router as users_router


app = FastAPI(title=settings.PROJECT_NAME, description=settings.DESCRIPTION)


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(users_router, prefix="/users", tags=["Users"])
