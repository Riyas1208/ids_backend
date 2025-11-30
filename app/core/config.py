import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    IDS_API_KEY: str | None = os.getenv("IDS_API_KEY")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "replace-me")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    MODEL_PATH: str = os.getenv("MODEL_PATH", "app/ml/rf_model.joblib")
    ALLOW_ORIGINS: list = ["*"]

settings = Settings()
