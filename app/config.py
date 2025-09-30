import os
from dotenv import load_dotenv

class Settings:
    GCP_PROJECT_ID: str = os.getenv("GCP_PROJECT_ID")
    FIRESTORE_DATABASE_ID: str = os.getenv("FIRESTORE_DATABASE_ID")

settings: Settings = Settings()