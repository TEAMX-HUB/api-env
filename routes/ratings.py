from fastapi import APIRouter, Depends
from psycopg import Connection

from compax_api.database import get_db_conn
import compax_api.utils
from compax_api.errors import InvalidRatingException

from schema.ratings import RateBuilding, RateClassroom, RateLaboratory, RateOffice

ratings = APIRouter()


@ratings.get("/ratings/", tags=["ratings"])
async def get_all_ratings(connection: Connection = Depends(get_db_conn)):
    res = compax_api.utils._get_all_and_execute("get_all_ratings.sql", connection)
    return res


@ratings.get("/rating/classroom/{classroom_id}", tags=["ratings"])
async def get_rating_for_classroom(
    classroom_id: int, connection: Connection = Depends(get_db_conn)
):
    res = compax_api.utils._get_all_and_execute_params(
        "get_all_ratings_classroom.sql", {"classroom_id": classroom_id}, connection
    )
    return res


@ratings.get("/rating/lab/{lab_id}", tags=["ratings"])
async def get_rating_for_lab(
    lab_id: int, connection: Connection = Depends(get_db_conn)
):
    res = compax_api.utils._get_all_and_execute_params(
        "get_all_ratings_lab.sql", {"lab_id": lab_id}, connection
    )
    return res


@ratings.get("/rating/building/{building_id}", tags=["ratings"])
async def get_rating_for_building(
    building_id: int, connection: Connection = Depends(get_db_conn)
):
    res = compax_api.utils._get_all_and_execute_params(
        "get_all_ratings_building.sql", {"building": building_id}, connection
    )
    return res


@ratings.get("/rating/office/{office_id}", tags=["ratings"])
async def get_rating_for_office(
    office_id: int, connection: Connection = Depends(get_db_conn)
):
    res = compax_api.utils._get_all_and_execute_params(
        "get_all_ratings_office.sql", {"office_id": office_id}, connection
    )
    return res


@ratings.post("/rating/new/classroom/", tags=["ratings"])
async def create_rating_for_classroom(
    classroom_rating: RateClassroom, connection: Connection = Depends(get_db_conn)
):
    results = compax_api.utils._insert_one_and_execute_params(
        filename="insert_into_ratings.sql",
        payload=classroom_rating.dict(),
        conn=connection,
    )
    if results:
        raise InvalidRatingException()
    return results


@ratings.post("/rating/new/lab/", tags=["ratings"])
async def create_rating_for_lab(
    lab_rating: RateLaboratory, connection: Connection = Depends(get_db_conn)
):
    results = compax_api.utils._insert_one_and_execute_params(
        filename="insert_into_ratings.sql", payload=lab_rating.dict(), conn=connection
    )
    if results:
        raise InvalidRatingException()
    return results


@ratings.post("/rating/new/building/", tags=["ratings"])
async def create_rating_for_building(
    building_rating: RateBuilding, connection: Connection = Depends(get_db_conn)
):
    results = compax_api.utils._insert_one_and_execute_params(
        filename="insert_into_ratings.sql",
        payload=building_rating.dict(),
        conn=connection,
    )
    if results:
        raise InvalidRatingException()
    return results


@ratings.post("/rating/new/office/", tags=["ratings"])
async def create_rating_for_office(
    office_rating: RateOffice, connection: Connection = Depends(get_db_conn)
):
    results = compax_api.utils._insert_one_and_execute_params(
        filename="insert_into_ratings.sql",
        payload=office_rating.dict(),
        conn=connection,
    )
    if results:
        raise InvalidRatingException()
    return results


@ratings.patch("/rating/{rating_id}", tags=["ratings"])
async def update_rating_comments(
    new_comment: str, rating_id: int, connection: Connection = Depends(get_db_conn)
):
    res = compax_api.utils._get_all_and_execute_params(
        "update_ratings_comments.sql",
        {"new_comment": new_comment, "rating_id": rating_id},
        connection,
    )
    return res
