class Fetch:
    def __init__(self,text,client,encoder):
        self.client = client
        self.encoder = encoder
        self.query_embedding = self.encoder.encode(text)
        self.hits = self.client.search(collection_name="Research_papers", query_vector=self.query_embedding,limit=1)
        self.score = self.hits[0].score
        self.number = self.hits[0].payload["number"]


#1)we have to do overall score
