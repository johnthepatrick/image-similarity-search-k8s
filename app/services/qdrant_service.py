import os
import requests


QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = os.getenv("QDRANT_PORT", "6333")
QDRANT_HEALTH_URL = f"http://{QDRANT_HOST}:{QDRANT_PORT}/healthz"


def check_qdrant_health() -> bool:
    try:
        response = requests.get(QDRANT_HEALTH_URL, timeout=5)
        response.raise_for_status()
        return True
    except requests.RequestException as error:
        print(f"Qdrant health check failed: {error}")
        return False