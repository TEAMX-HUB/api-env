from uuid import UUID

from fastapi import APIRouter, Depends
from psycopg import Connection

from compax_api.database import get_db_conn
from compax_api.errors import UserNotFoundException

user = APIRouter()


@user.get("/i/", tags=["users"])
async def get_user_by_reference(
    reference: int, connection: Connection = Depends(get_db_conn)
):
    # insert connection query in here.
    res = connection.execute()

    if res is None:
        raise UserNotFoundException(user_id=reference)

    # handle errors properly
    return res


@user.get("/i/", tags=["users"])
async def get_user_by_uuid(uuid: UUID, connection: Connection = Depends(get_db_conn)):
    # insert connection query in here.
    res = connection.execute()

    if res is None:
        raise UserNotFoundException(user_id=uuid)

    # handle errors properly
    return res
