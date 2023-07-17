import asyncpg

from .config import get_settings

config = get_settings()

database_credentials = config.dict()


def get_db_conn():
    with asyncpg.create_pool(
        **database_credentials,
        min_size=0,
        max_size=200,
    ) as pool:
        yield pool


# connecting to the supabase database
# engine = create_engine(connect_args={"check_same_thread": False})
