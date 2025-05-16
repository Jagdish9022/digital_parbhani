from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from app.db.models import Service
import uuid
from qdrant_client.http.exceptions import UnexpectedResponse

client = QdrantClient(host="localhost", port=6333)  # Assuming Qdrant is running locally

COLLECTION_NAME = "services"

try:
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=2, distance=Distance.EUCLID),
    )
except Exception as e:
    if "already exists" not in str(e).lower():
        raise e

def insert_services(services: list[Service]):
    points = [
        PointStruct(
            id=str(uuid.uuid4()),
            vector=[s.latitude, s.longitude],
            payload=s.dict()
        )
        for s in services
    ]
    client.upsert(collection_name=COLLECTION_NAME, points=points)

def search_nearby(lat: float, lon: float, top_k: int = 100):  # increased from 5 to 100
    hits = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=[lat, lon],
        limit=top_k
    )
    return [hit.payload for hit in hits]
