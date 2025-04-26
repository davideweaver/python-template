from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import os
from dotenv import load_dotenv

# load .env.local manually first, if it exists
if os.path.exists(".env.local"):
    load_dotenv(".env.local", override=True)


class Settings(BaseSettings):
    ENV: str = "development"
    PORT: int = 8000
    DEBUG: bool = False

    SECRET_KEY: str
    DB_URL: str

    model_config = SettingsConfigDict(
        env_file=(
            ".env",
            f".env.{os.getenv('ENV', 'development')}",
        ),
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


@lru_cache
def get_settings():
    return Settings()
