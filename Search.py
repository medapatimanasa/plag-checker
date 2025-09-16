import json
from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer
import time


class Search:

    def __init__(self, text, data):
        self.encoder = SentenceTransformer("all-MiniLM-L6-v2")
        self.qdrant = QdrantClient(":memory:")
        self.qdrant.create_collection(
            collection_name="Research_papers",
            vectors_config=models.VectorParams(
                size=self.encoder.get_sentence_embedding_dimension(),
                distance=models.Distance.COSINE,
                on_disk=True
            ),
        )
        self.qdrant.upload_points(
            collection_name="Research_papers",
            points=[
                models.PointStruct(
                    id=idx, vector=self.encoder.encode(doc["text"]).tolist(), payload=doc)
                for idx, doc in enumerate(data)
            ],
        )
        self.result = self.search(text)

    def search(self, text):
        start_time = time.perf_counter()

        hits = self.qdrant.search(
            collection_name="Research_papers",
            query_vector=self.encoder.encode(text).tolist(),
            limit=1,
        )
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(elapsed_time)

        return [hits[0].score, hits[0].payload['number']]



