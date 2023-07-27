from fastapi import APIRouter, Depends
from psycopg import Connection

import compax_api.utils
from compax_api.database import get_db_conn
from compax_api.errors import AuthInvalidCredentialsException
from schema.user import AdminCreate, ExamOfficerCreate

admin = APIRouter()


@admin.post("/i/admin/new", tags=["users"])
async def create_admin(
    new_user: AdminCreate, connection: Connection = Depends(get_db_conn)
):
    results = compax_api.utils._insert_one_and_execute_params(
        filename="insert_into_users.sql", payload=new_user.dict(), conn=connection
    )
    if results:
        raise AuthInvalidCredentialsException
    return results


@admin.post("/i/officer/new", tags=["users"])
async def create_officer(
    new_user: ExamOfficerCreate, connection: Connection = Depends(get_db_conn)
):
    results = compax_api.utils._insert_one_and_execute_params(
        filename="insert_into_users.sql", payload=new_user.dict(), conn=connection
    )
    if results:
        raise AuthInvalidCredentialsException
    return results
