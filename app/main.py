
from fastapi import FastAPI

from api.routes import router
from core.config import APP_NAME, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    description="A cloud-native image similarity search API using FastAPI, CLIP, Qdrant and Kubernetes.",
    version=APP_VERSION,
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Image Similarity SEARCH API!",
        "docs": "/docs",
        "health":"/health",
        }

app.include_router(router)