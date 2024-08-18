import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://library_user:1234567890@localhost:5432/library_db")

settings = Settings()
