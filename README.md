# Image Similarity Search API

Aktueller Entwicklungsstand einer cloud-nativen API zur Bildähnlichkeitssuche mit FastAPI, CLIP, Qdrant und Kubernetes.

## Aktueller Stand

Derzeit sind folgende Bestandteile umgesetzt:

- FastAPI-Anwendung mit Root- und Health-Endpunkt
- lokaler Qdrant-Betrieb über Docker Compose
- konfigurierbare Verbindung zu Qdrant über Umgebungsvariablen
- Qdrant-Healthcheck
- Funktionen zum Anlegen und Löschen der Collection `image_vectors`
- Vektorkonfiguration mit 512 Dimensionen und Dot-Product-Distanz

Die Funktionen zum Anlegen und Löschen der Collection sind aktuell nur im Service definiert. Sie werden noch nicht automatisch beim Anwendungsstart ausgeführt und sind nicht als API-Endpunkte verfügbar.

## Projektstruktur

```text
app/
├── api/
│   └── routes.py             # API-Routen und Health-Endpunkt
├── core/
│   └── config.py             # Anwendungsname und Version
├── services/
│   └── qdrant_service.py     # Qdrant-Verbindung und Collection-Verwaltung
└── main.py                    # FastAPI-Anwendung
docker-compose.yaml              # Lokale Qdrant-Instanz
requirements.txt                 # Python-Abhängigkeiten
```

## Voraussetzungen

- Python mit den Paketen aus `requirements.txt`
- Docker mit Docker Compose

Das lokale Conda-Environment für das Projekt heißt derzeit `image-similarity`.

## Lokale Einrichtung

Conda-Environment aktivieren und Abhängigkeiten installieren:

```bash
conda activate image-similarity
pip install -r requirements.txt
```

Qdrant starten:

```bash
docker compose up -d qdrant
```

Die REST-Schnittstelle von Qdrant ist danach unter `http://localhost:6333` erreichbar. Der gRPC-Port ist `6334`.

FastAPI aus dem Verzeichnis `app` starten:

```bash
cd app
uvicorn main:app --reload
```

Danach stehen folgende Endpunkte zur Verfügung:

- `GET /` – grundlegende Informationen zur API
- `GET /health` – Status der API und der Qdrant-Abhängigkeit
- `GET /docs` – interaktive OpenAPI-Dokumentation

## Qdrant-Konfiguration

Die Verbindung wird über folgende Umgebungsvariablen konfiguriert:

| Variable | Standardwert | Bedeutung |
| --- | --- | --- |
| `QDRANT_HOST` | `localhost` | Hostname der Qdrant-Instanz |
| `QDRANT_PORT` | `6333` | REST-Port der Qdrant-Instanz |

Beispiel:

```bash
export QDRANT_HOST=localhost
export QDRANT_PORT=6333
```

## Collection-Verwaltung

`app/services/qdrant_service.py` stellt derzeit drei Funktionen bereit:

- `check_qdrant_health()` prüft den Qdrant-Endpunkt `/healthz`.
- `create_qdrant_collection()` legt `image_vectors` an, sofern die Collection noch nicht existiert.
- `delete_qdrant_collection()` löscht `image_vectors`, sofern die Collection existiert.

Die Collection wird mit folgender Vektorkonfiguration angelegt:

```text
Name:       image_vectors
Dimension:  512
Distanz:    Dot Product
```

Die Dimension eines später gespeicherten Vektors muss exakt zur konfigurierten Dimension `512` passen.

> Achtung: `delete_qdrant_collection()` entfernt die gesamte Collection `image_vectors` einschließlich aller darin gespeicherten Punkte.

## Noch nicht umgesetzt

- automatische Initialisierung der Collection beim Start der API
- Endpunkte zum Hinzufügen und Suchen von Bildvektoren
- Erzeugung von Bild-Embeddings mit CLIP
- Kubernetes-Deployment
- automatisierte Tests
