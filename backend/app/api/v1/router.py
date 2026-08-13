from fastapi import APIRouter

from backend.app.api.v1.endpoints.health import router as health_router
from backend.app.api.v1.endpoints.user import router as user_router
from backend.app.api.v1.endpoints.auth import router as auth_router
from backend.app.api.v1.endpoints.address import (
    router as address_router,
)
from backend.app.api.v1.endpoints.upload import router as upload_router
from backend.app.api.v1.endpoints.agent import router as agent_router


api_router = APIRouter()



api_router.include_router(
    health_router,
    tags=["Health"],
)

api_router.include_router(
    user_router,
    tags=["Users"],
)

api_router.include_router(
    auth_router,
    tags=["Authentication"],
)

api_router.include_router(
    address_router,
)

api_router.include_router(
    upload_router,
)

api_router.include_router(agent_router)

@api_router.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "service": "Data Ops AI",
        "version": "1.0.0"
    }