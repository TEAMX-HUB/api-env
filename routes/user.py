from uuid import uuid4 as UUID

from asyncpg import Pool
from fastapi import APIRouter, Depends

from compax_api.database import get_db_conn
from compax_api.errors import UserNotFoundException

user = APIRouter()


@user.get("/i/{user_id}", tags=["users"])
async def get_user(user_id: UUID, connection: Pool = Depends(get_db_conn)):
    # insert connection query in here.
    res = await connection.execute()

    if res is None:
        raise UserNotFoundException(user_id=user_id)

    # handle errors properly
    return res
