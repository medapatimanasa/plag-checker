from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer
import json

file_path = "embeddings_1.txt"
documents = []
with open(file_path, "r") as file:
    for line in file:
        json_data = json.loads(line)
        documents .append(json_data)

encoder = SentenceTransformer("all-MiniLM-L6-v2")
client = QdrantClient(path="Qdrant_db")
client.create_collection(
    collection_name="Research_papers",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),
        distance=models.Distance.COSINE,
    ),
)
client.upsert(
    collection_name="Research_papers",
    points=[
        models.PointStruct(
            id=idx, vector=encoder.encode(doc["text"]).tolist(), payload=doc)
        for idx, doc in enumerate(documents)
    ],
)

