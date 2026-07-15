from fastapi import APIRouter

from services.qdrant_service import check_qdrant_health

router = APIRouter()

@router.get("/health")
async def health_check():
    qdrant_healthy = check_qdrant_health()
    
    return {
        "status": "ok" if qdrant_healthy else "degraded",
        "service": "image-similarity-search-api",
        "dependencies": {
            "qdrant": "ok" if qdrant_healthy else "unavailable"
        }
    }