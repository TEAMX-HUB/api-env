from fastapi import APIRouter, Depends
from psycopg import Connection
from supabase import Client, create_client

import routes.admin
import routes.user
from compax_api.config import get_settings
from compax_api.database import get_db_conn
from compax_api.errors import (
    AuthInvalidCredentialsException,
    UserReferenceFoundException,
    UserNotFoundException,
)
from compax_api.security import Password
from schema.user import AdminCreate, ExamOfficerCreate, UserCreate

config = get_settings()

auth = APIRouter()

url, key = config.supabase_client_url, config.supabase_client_key
supabase: Client = create_client(supabase_url=url, supabase_key=key)


@auth.get("/auth/signin", tags=["auth"])
async def sign_in(
    reference: str, password: str, connection: Connection = Depends(get_db_conn)
):
    user = routes.user.get_user_by_reference(reference=reference, connection=connection)
    if user is None:
        raise UserReferenceFoundException(ref=reference)

    data = UserCreate(**user[0])

    if Password.verify(plain=password, hashed=data.password):
        res = await supabase.auth.sign_in_with_password(
            {
                "email": data.username,
                "password": password,
                "email_confirm": False,
            }
        )
    else:
        raise UserNotFoundException(message="User with password cannot be found!")
    return res


@auth.post("/auth/signout", tags=["auth"])
async def sign_out(username: str):
    res = supabase.auth.sign_out()
    return res


@auth.post("/auth/signup", tags=["auth"])
async def sign_up(new_user: UserCreate, connection: Connection = Depends(get_db_conn)):
    auth_response = _supabase_authenticate(new_user=new_user)
    extracted_id = auth_response.dict()["user"]["id"]
    new_user.id = extracted_id
    new_user.password = Password.hash(new_user.password)
    routes.user.create_user(new_user, connection)


def _supabase_authenticate(new_user: UserCreate):
    auth_response = supabase.auth.sign_up(
        {
            "email": new_user.username + "@st.knust.edu.gh",
            "password": Password.hash(password=new_user.password),
        }
    )
    if auth_response is None:
        raise AuthInvalidCredentialsException
    return auth_response


@auth.post("/auth/admin/signup", tags=["auth"])
async def sign_up_admin(
    new_user: AdminCreate, connection: Connection = Depends(get_db_conn)
):
    auth_response = _supabase_authenticate(new_user=new_user)
    extracted_id = auth_response.dict()["user"]["id"]
    new_user.id = extracted_id
    routes.admin.create_admin(new_user, connection)


@auth.post("/auth/officer/signup", tags=["auth"])
async def sign_up_examofficer(
    new_user: ExamOfficerCreate, connection: Connection = Depends(get_db_conn)
):
    auth_response = _supabase_authenticate(new_user=new_user)
    extracted_id = auth_response.dict()["user"]["id"]
    new_user.id = extracted_id
    routes.admin.create_officer(new_user, connection)
