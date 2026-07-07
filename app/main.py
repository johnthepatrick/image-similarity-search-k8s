
from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="Image Similarity SEARCH API",
    description="A cloud-native image similarity search API using FastAPI, CLIP, Qdrant and Kubernetes.",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Image Similarity SEARCH API!",
        "docs": "/docs",
        "health":"/health",
        }

app.include_router(router)