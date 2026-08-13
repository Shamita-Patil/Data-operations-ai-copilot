from fastapi import APIRouter

from backend.app.services.health_service import HealthService

router = APIRouter()

health_service = HealthService()


@router.get("/health")
def health():
    return health_service.get_application_health()
