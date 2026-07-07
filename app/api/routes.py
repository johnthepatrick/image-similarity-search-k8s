from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok", "message": "API is healthy and running."}

