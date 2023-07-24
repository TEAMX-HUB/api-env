import psycopg
from psycopg.rows import dict_row

from .config import get_settings

config = get_settings()

database_credentials: str = config.dict()["db_url"]


# try caching the connection
def get_db_conn():
    with psycopg.connect(
        database_credentials,
        row_factory=dict_row,
    ) as conn:
        yield conn


# connecting to the supabase database
# engine = create_engine(connect_args={"check_same_thread": False})
