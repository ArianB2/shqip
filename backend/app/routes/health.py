from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/health")
def health_check():
    """
    Health check endpoint.
    AWS ECS and load balancers ping this to confirm the app is running.
    Always keep this fast and dependency-free.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "app": "shqip-api",
    }
