from sqlalchemy import create_engine

from .config import get_settings

# connecting to the supabase database
engine = create_engine(
    get_settings().supabase_uri, connect_args={"check_same_thread": False}
)
