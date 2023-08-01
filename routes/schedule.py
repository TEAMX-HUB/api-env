from fastapi import APIRouter, Depends
from compax_api.database import get_db_conn
import compax_api.utils
from psycopg import Connection
from datetime import datetime, time

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


@schedule.get("/schedule/", tags=["schedule"])
async def get_all_schedule(connection: Connection = Depends(get_db_conn)):
    res = compax_api.utils._get_all_and_execute("get_all_schedule.sql", connection)
    return res


@schedule.get("/schedule/day/{weekday}", tags=["schedule"])
async def get_all_schedule_for_day(
    weekday: str, connection: Connection = Depends(get_db_conn)
):
    res = compax_api.utils._get_all_and_execute_params(
        "get_schedule_all_for_day.sql", {"weekday": weekday}, connection
    )
    return res


@schedule.get("/schedule/all/{weekday}", tags=["schedule"])
async def get_schedule_all_for_session(
    weekday: str,
    start_time: time,
    end_time: time,
    connection: Connection = Depends(get_db_conn),
):
    res = compax_api.utils._get_all_and_execute_params(
        "get_schedule_all_for_day.sql",
        {"weekday": weekday, "start_time": start_time, "end_time": end_time},
        connection,
    )
    return res


@schedule.get("/i/schedule/day/", tags=["schedule"])
async def get_schedule_day_with_user_data(
    year_group: int,
    department: str,
    connection: Connection = Depends(get_db_conn),
):
    weekday = WEEKDAYS[datetime.now().weekday()]
    res = compax_api.utils._get_all_and_execute_params(
        "get_schedule_day_with_user_data.sql",
        {"weekday": weekday, "year_group": year_group, "department": department},
        connection,
    )
    return res


@schedule.get("/schedule/class/{classroom_id}", tags=["schedule"])
async def get_schedule_for_classroom(
    classroom_id: int, connection: Connection = Depends(get_db_conn)
):
    weekday = WEEKDAYS[datetime.now().weekday()]
    res = compax_api.utils._get_all_and_execute_params(
        "get_schedule_for_classroom.sql",
        {"weekday": weekday, "classroom_id": classroom_id},
        connection,
    )
    return res


@schedule.get("/schedule/building/{building_id}", tags=["schedule"])
async def get_schedule_for_building(
    building_id: int, connection: Connection = Depends(get_db_conn)
):
    weekday = WEEKDAYS[datetime.now().weekday()]
    res = compax_api.utils._get_all_and_execute_params(
        "get_schedule_for_building.sql",
        {"weekday": weekday, "building_id": building_id},
        connection,
    )
    return res


@schedule.get("/schedule/lab/{lab_id}", tags=["schedule"])
async def get_schedule_for_lab(
    lab_id: int, connection: Connection = Depends(get_db_conn)
):
    weekday = WEEKDAYS[datetime.now().weekday()]
    res = compax_api.utils._get_all_and_execute_params(
        "get_schedule_for_lab.sql",
        {"weekday": weekday, "lab_id": lab_id},
        connection,
    )
    return res


@schedule.get("/i/schedule/", tags=["schedule"])
async def get_schedule_with_user_data(
    year_group: int,
    department: str,
    connection: Connection = Depends(get_db_conn),
):
    res = compax_api.utils._get_all_and_execute_params(
        "get_schedule_with_user_data.sql",
        {"year_group": year_group, "department": department},
        connection,
    )
    return res
