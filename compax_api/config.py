from functools import lru_cache
from pathlib import Path

from pydantic import BaseSettings

base_env = Path("../.env")


class Settings(BaseSettings):
    env_name: str = ""
    supabase_uri: str = ""
    supabase_key: str = ""

    class Config:
        # allows the import of environment variables from .env
        # env file has variables included as attributes in
        # this class and more. you can decide to go with the
        # default preset used above or set your own .env file
        env_file = base_env
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
