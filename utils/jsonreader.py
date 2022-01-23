import json


class JsonReader:
    def __init__(self, file_name):
        with open(file_name) as json_file:
            self.data = json.load(json_file)

    def __getitem__(self, item):
        return self.data[item]
