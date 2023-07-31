from uuid import UUID

from fastapi import APIRouter, Depends
from psycopg import Connection

import compax_api.utils
from compax_api.security import Password
from compax_api.database import get_db_conn
from compax_api.errors import (
    UserNameNotFoundException,
    UserNotFoundException,
    UserReferenceFoundException,
    AuthInvalidCredentialsException,
)
from schema.user import UserCreate

user = APIRouter()


@user.get("/i/{reference}", tags=["users"])
def get_user_by_reference(
    reference: int, connection: Connection = Depends(get_db_conn)
):
    res = compax_api.utils._get_one_and_execute_params(
        "get_user_reference.sql", {"student_reference": reference}, connection
    )

    if res is None:
        raise UserReferenceFoundException(ref=reference)

    return res


@user.get("/i/{uuid}", tags=["users"], deprecated=True)
async def get_user_by_uuid(
    uuid: UUID,
    connection: Connection = Depends(get_db_conn),
):
    res = compax_api.utils._get_one_and_execute_params(
        "get_user_uuid.sql", {"id": uuid}, connection
    )

    if res is None:
        raise UserNotFoundException(user_id=uuid)

    return res


@user.get("/i/{username}", tags=["users"], deprecated=True)
async def get_user_by_username(
    username: str,
    connection: Connection = Depends(get_db_conn),
):
    res = compax_api.utils._get_one_and_execute_params(
        "get_user_username.sql", {"username": username}, connection
    )

    if res is None:
        raise UserNameNotFoundException(username=username)

    return res


@user.post("/i/new", tags=["users"])
async def create_user(
    new_user: UserCreate, connection: Connection = Depends(get_db_conn)
):
    results = compax_api.utils._insert_one_and_execute_params(
        filename="insert_into_users.sql", payload=new_user.dict(), conn=connection
    )
    if results is None:
        raise AuthInvalidCredentialsException
    return results


@user.get("/i/pd_check/{reference}", tags=["users"], deprecated=True)
async def check_user_validity(
    reference: int, password: str, connection: Connection = Depends(get_db_conn)
):
    user = get_user_by_reference(reference=reference, connection=connection)
    if user is None:
        raise UserReferenceFoundException(ref=reference)

    data = UserCreate(**user)

    if Password.verify(plain=password, hashed=data.password):
        return True
    else:
        raise UserNotFoundException(message="User with password cannot be found!")
