from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        load_dotenv()

    @property
    def yandex_api_key(self) -> str:
        return os.getenv('YANDEX_CLOUD_API_KEY')