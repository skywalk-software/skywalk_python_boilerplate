import os

from dotenv import load_dotenv


def load_config():
    load_dotenv()
    return {
        "API_KEY": os.getenv("API_KEY"),
        "SECRET_KEY": os.getenv("SECRET_KEY"),
    }
