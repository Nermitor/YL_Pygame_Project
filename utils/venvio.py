import os

import dotenv


class VenvIO:
    def __init__(self):
        self.dotenv_file = dotenv.find_dotenv()
        dotenv.load_dotenv()

    @staticmethod
    def get_value(key):
        return os.getenv(key)

    def set_value(self, key, value):
        os.environ[key] = value
        dotenv.set_key(self.dotenv_file, key, value)
