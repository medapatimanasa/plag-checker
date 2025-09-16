from Extract import Paper
from pathlib import Path
import json


class Data:
    def __init__(self):
        self._data = [Paper(path).__dict__() for path in Path("data_set").rglob('*.json')]
        self.json_list = [json.dumps(obj) for obj in self._data]
        with open("embeddings_1.txt", "w") as file:
            for line in self.json_list:
                file.write(line + "\n")

    def get_data(self):
        return self._data
