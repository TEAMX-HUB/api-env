from fastapi import APIRouter, Depends
from psycopg import Connection

from compax_api.database import get_db_conn
from schema.classroom import Classroom
import compax_api.utils

classroom = APIRouter()

# GET /classrooms: Retrieves a list of available classrooms.
# GET /classrooms/{id}: Retrieves detailed information about a specific classroom.
# POST /classrooms: Creates a new classroom.
# PUT /classrooms/{id}: Updates the details of a specific classroom.
# DELETE /classrooms/{id}: Deletes a specific classroom.


@classroom.get("/classrooms/", tags=["classrooms"])
async def get_all_classrooms(connection: Connection = Depends(get_db_conn)):
    res = compax_api.utils._get_all_and_execute("get_all_classrooms.sql", connection)
    return res


@classroom.get("/classroom/{classroom_id}", tags=["classrooms"])
async def get_classroom(
    classroom_id: int, connection: Connection = Depends(get_db_conn)
):
    res = compax_api.utils._get_one_and_execute_params(
        "get_classroom_with_id.sql", {"classroom_id": classroom_id}, connection
    )
    return res


@classroom.get("/classroom/", tags=["classrooms"])
async def search_classroom_with_name(
    name: str, connection: Connection = Depends(get_db_conn)
):
    name = f"%{name}%"
    res = compax_api.utils._get_all_and_execute_params(
        "get_classroom_with_name.sql", {"name": name}, connection
    )
    return res


@classroom.get("/classrooms/{building_id}", tags=["classrooms"])
async def get_all_classrooms_in_building(
    building_id: int, connection: Connection = Depends(get_db_conn)
):
    pass


@classroom.post("/classrooms/new", tags=["classrooms"])
async def create_classroom(
    new_classroom: Classroom, connection: Connection = Depends(get_db_conn)
):
    pass


@classroom.patch("/classroom/image/{classroom_id}", tags=["classrooms"])
async def update_classsroom_image(
    classroom_id: int, connection: Connection = Depends(get_db_conn)
):
    pass


@classroom.delete("/classrooms/{classroom_id}", tags=["classrooms"])
async def delete_classroom(
    classroom_id: int, connection: Connection = Depends(get_db_conn)
):
    pass


# @classroom.get("/search/classrooms/")
# def query_classrooms_by_parameters(
#     name: str | None,
# ) -> dict[str, Classroom | list[Classroom]]:
#     classrooms = get_all_classrooms()

#     if name is None:
#         return classrooms

#     def check_item(classroom: Classroom, connection: Connection = Depends(get_db_conn)):
#         return (name is None or classroom.name == name,)

#     selection = [item for item in classrooms if check_item(item)]
#     return {
#         "query": {"name": name},
#         "selection": selection,
#     }
