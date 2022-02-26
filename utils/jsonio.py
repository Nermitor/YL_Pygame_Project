"""Позволяет читать и изменять json-файл"""

import json


class JsonIO:
    def __init__(self, file_name):
        self.file_name = file_name
        with open(file_name) as json_file:
            self.data = json.load(json_file)

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value
        with open(self.file_name, 'w') as file:
            json.dump(self.data, file)

    def save(self, d):
        with open(self.file_name, 'w') as file:
            json.dump(d, file)
