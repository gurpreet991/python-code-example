from functools import lru_cache
from pydantic_settings import BaseSettings
from fastapi.middleware.cors import CORSMiddleware


class Settings(BaseSettings):
    DEBUG: bool

    CURRENT_VERSION: int = 1

    OPEN_AI_KEY: str
    OPEN_ASSISSTANT_ID: str
    AI_PROMPT: str
    AI_LIMIT: str

    SUPPORT: str

    POSTMARK_TESTING_EMAIL: str

    POSTMARK_LIVE_TOKEN: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


cors_config = {
    "middleware_class": CORSMiddleware,
    "allow_origins": ["*"],
    "allow_methods": ["*"],
    "allow_headers": ["*"],
    "allow_credentials": True,
}
