from fastapi import APIRouter, Depends
from compax_api.database import get_db_conn
from psycopg import Connection
from datetime import datetime

schedule = APIRouter()

WEEKDAYS = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


@schedule.get("/schedule/{weekday}", tags=["schedule"])
async def get_all_schedule_for_day(
    weekday: str, connection: Connection = Depends(get_db_conn)
):
    pass


@schedule.get("/schedule/{weekday}", tags=["schedule"])
async def get_schedule_day_with_user_data(
    weekday: str,
    year_group: int,
    department: str,
    connection: Connection = Depends(get_db_conn),
):
    weekday = WEEKDAYS[datetime.now().weekday()]
    return weekday
