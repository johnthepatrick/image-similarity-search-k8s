from fastapi import APIRouter, HTTPException

from app.services import qdrant_health_check

router = APIRouter()

@router.get("/health")
async def health_check():
    qdrant_healthy = qdrant_health_check.check_qdrant_health()
    
    return {
        "status": "ok" if qdrant_healthy else "degraded",
        "service": "image-similarity-search-api",
        "dependencies": {
            "qdrant": "ok" if qdrant_healthy else "unavailable"
        }
    }

