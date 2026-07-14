import os
import requests

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams


QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = os.getenv("QDRANT_PORT", "6333")
QDRANT_HEALTH_URL = f"http://{QDRANT_HOST}:{QDRANT_PORT}/healthz"

client = QdrantClient(
    host=QDRANT_HOST,
    port=QDRANT_PORT
    )

def check_qdrant_health() -> bool:
    try:
        response = requests.get(QDRANT_HEALTH_URL, timeout=5)
        response.raise_for_status()
        return True
    except requests.RequestException as error:
        print(f"Qdrant health check failed: {error}")
        return False
    
def create_qdrant_collection() -> bool:
    collection_name = "image_vectors"

    try:
        if client.collection_exists(collection_name):
            print(f"Qdrant collection '{collection_name}' already exists")
            return True

        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=512,
                distance=Distance.DOT,
            ),
        )

        print(f"Qdrant collection '{collection_name}' created")
        return True

    except Exception as error:
        print(f"Failed to create Qdrant collection: {error}")
        return False