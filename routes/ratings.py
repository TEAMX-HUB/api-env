from fastapi import APIRouter, Depends
from psycopg import Connection
from compax_api.database import get_db_conn

ratings = APIRouter()


@ratings.get("/ratings/", tags=["ratings"])
async def get_all_ratings(connection: Connection = Depends(get_db_conn)):
    pass


@ratings.get("/rating/classroom/{id}", tags=["ratings"])
async def get_rating_for_classroom(
    classroom_id: int, connection: Connection = Depends(get_db_conn)
):
    pass


@ratings.get("/rating/lab/{id}", tags=["ratings"])
async def get_rating_for_lab(
    lab_id: int, connection: Connection = Depends(get_db_conn)
):
    pass


@ratings.get("/rating/building/{id}", tags=["ratings"])
async def get_rating_for_building(
    classroom_id: int, connection: Connection = Depends(get_db_conn)
):
    pass


@ratings.get("/rating/office/{id}", tags=["ratings"])
async def get_rating_for_office(
    classroom_id: int, connection: Connection = Depends(get_db_conn)
):
    pass


@ratings.post("/rating/new/classroom/{id}", tags=["ratings"])
async def create_rating_for_classroom(
    classroom_id: int, connection: Connection = Depends(get_db_conn)
):
    pass


@ratings.post("/rating/new/lab/{id}", tags=["ratings"])
async def create_rating_for_lab(
    lab_id: int, connection: Connection = Depends(get_db_conn)
):
    pass


@ratings.post("/rating/new/building/{id}", tags=["ratings"])
async def create_rating_for_building(
    classroom_id: int, connection: Connection = Depends(get_db_conn)
):
    pass


@ratings.post("/rating/new/office/{id}", tags=["ratings"])
async def create_rating_for_office(
    classroom_id: int, connection: Connection = Depends(get_db_conn)
):
    pass
