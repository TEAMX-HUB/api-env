from fastapi import APIRouter
from supabase import Client, create_client

from compax_api.config import get_settings
from compax_api.errors import InvalidCredentialsException
from compax_api.security import Password
from schema.user import AdminCreate, ExamOfficerCreate, UserCreate

config = get_settings()

auth = APIRouter()

url, key = config.supabase_client_url, config.supabase_client_key
supabase: Client = create_client(supabase_url=url, supabase_key=key)


@auth.get("/auth/signin", tags=["auth"])
async def sign_in(username: str, password: str):
    # do not store bare password keywords
    # always sign_up and sign_in with the hash
    # do not forget to disable email confirmations
    res = await supabase.auth.sign_in_with_password(
        {"email": username, "password": Password.hash(password=password)}
    )
    return res


@auth.post("/auth/signup", tags=["auth"])
async def sign_up(new_user: UserCreate):
    details = new_user.dict()

    # authentication should have it's own sign_up
    auth_res = await supabase.auth.sign_up(
        {
            "email": new_user.username,
            "password": Password.hash(password=new_user.password),
        }
    )

    if auth_res:
        # handle any errors from this end
        raise InvalidCredentialsException

    # cater for sign_up on sign_up table
    data, count = await supabase.table("users").insert(details).execute()

    return auth_res


@auth.post("/auth/admin/signup", tags=["auth"])
async def sign_up_admin(new_user: AdminCreate):
    pass


@auth.post("/auth/officer/signup", tags=["auth"])
async def sign_up_examofficer(new_user: ExamOfficerCreate):
    pass


# @auth.get()
