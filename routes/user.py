from uuid import UUID

from fastapi import APIRouter, Depends
from psycopg import Connection

import compax_api.utils
from compax_api.database import get_db_conn
from compax_api.errors import (
    UserNameNotFoundException,
    UserNotFoundException,
    UserReferenceFoundException,
)
from schema.user import UserCreate

user = APIRouter()


@user.get("/i/{reference}", tags=["users"])
def get_user_by_reference(
    reference: int, connection: Connection = Depends(get_db_conn)
):
    # create script to extract uuid
    res = compax_api.utils._get_one_and_execute_params(
        "get_user_reference.sql", {"student_reference": reference}, connection
    )

    if res is None:
        raise UserReferenceFoundException(ref=reference)

    return res


@user.get("/i/{uuid}", tags=["users"])
async def get_user_by_uuid(uuid: UUID, connection: Connection = Depends(get_db_conn)):
    # create script to extract uuid
    res = compax_api.utils._get_one_and_execute_params(
        "get_user_uuid.sql", {"id": uuid}, connection
    )

    if res is None:
        raise UserNotFoundException(user_id=uuid)

    return res


@user.get("/i/{username}", tags=["users"])
async def get_user_by_username(
    username: str, connection: Connection = Depends(get_db_conn)
):
    res = compax_api.utils._get_one_and_execute_params(
        "get_user_username.sql", {"username": username}, connection
    )

    if res is None:
        raise UserNameNotFoundException(username=username)

    return res


@user.post("/i/new", tags=["users"])
def create_user(new_user: UserCreate, connection: Connection = Depends(get_db_conn)):
    new_user.username += "@st.knust.edu.gh"
    compax_api.utils._insert_parse_and_execute(
        filename="insert_into_users.sql", payload=new_user.dict(), conn=connection
    )
