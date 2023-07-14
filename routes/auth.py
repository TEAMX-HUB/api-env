from fastapi import APIRouter
from supabase import Client, create_client

from compax_api.config import get_settings

config = get_settings()

auth = APIRouter()

url, key = config.supabase_uri, config.supabase_key
supabase: Client = create_client(supabase_url=url, supabase_key=key)


@auth.get("", tags=["auth"])
async def login():
    pass
