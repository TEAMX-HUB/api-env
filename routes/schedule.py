from fastapi import APIRouter, Depends
from compax_api.database import get_db_conn
from psycopg import Connection

schedule = APIRouter()


@schedule.get("/schedule/{weekday}", tags=["schedule"])
async def get_all_schedule_for_day(
    weekday: str, connection: Connection = Depends(get_db_conn)
):
    pass
