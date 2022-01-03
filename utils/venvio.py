import os

import dotenv


class VenvIO:
    def __init__(self):
        self.dotenv_file = dotenv.find_dotenv()
        dotenv.load_dotenv()

    def __getitem__(self, item):
        return os.getenv(item)

    def __setitem__(self, key, value):
        os.environ[key] = value
        dotenv.set_key(self.dotenv_file, key, value)
