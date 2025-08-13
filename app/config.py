from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    ROUTES_PATH = os.getenv("ROUTES_PATH", "data/routes.json")

settings = Settings()
