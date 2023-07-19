from functools import lru_cache
from pathlib import Path

from pydantic import BaseSettings

cwd = Path.cwd()
base_env = cwd / ".env"
prod_env = cwd / "prod.env"  # don't forget to set to prod.env when deploying


class Settings(BaseSettings):
    env_name: str = ""
    supabase_client_url: str = ""
    supabase_client_key: str = ""
    db_url: str = ""
    db_name: str = ""
    db_user: str = ""
    db_port: int = 0
    db_password: str = ""
    db_host: str = ""

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
