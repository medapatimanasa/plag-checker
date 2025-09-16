from Extract_User import TextExtractor
from Fetch_Score import Fetch
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer


class Output :

    def __init__(self,file_path):
        self.client = QdrantClient(path="Qdrant_db")
        self.encoder = SentenceTransformer("all-MiniLM-L6-v2")
        self.script = self.get_the_text(file_path)
        self.output = self.fn(self.script)



    def get_the_text(self,file_path):
        script = TextExtractor(file_path).text
        return script

    def fn(self,script):
        final_string = []
        final_score = 0
        split_sentences = script.split(".")
        val = len(split_sentences)
        for i in split_sentences:
            temp = Fetch(i, self.client, self.encoder)
            score = temp.score
            id = temp.number
            final_score += score
            if score > 0.5:
                final_string += [{'text': f"{i}",'id':id, 'present':1}]
            else:
                final_string += [{'text': f"{i}",'id':0,'present':0}]

        final_score /= val
        final_score *= 100
        return final_string, final_score
