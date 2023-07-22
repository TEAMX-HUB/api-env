from fastapi import APIRouter, Depends
from psycopg import Connection

from compax_api.database import get_db_conn
from schema.classroom import Classroom

classroom = APIRouter()

# GET /classrooms: Retrieves a list of available classrooms.
# GET /classrooms/{id}: Retrieves detailed information about a specific classroom.
# POST /classrooms: Creates a new classroom.
# PUT /classrooms/{id}: Updates the details of a specific classroom.
# DELETE /classrooms/{id}: Deletes a specific classroom.


@classroom.get("/classrooms/", tags=["classrooms"])
async def get_all_classrooms(connection: Connection = Depends(get_db_conn)):
    pass


@classroom.get("/classroom/{classroom_id}", tags=["classrooms"])
async def get_classroom(
    classroom_id: int, connection: Connection = Depends(get_db_conn)
):
    pass


@classroom.put("/classrooms/{classroom_id}", tags=["classrooms"])
async def update_classroom(
    classroom_id: int, connection: Connection = Depends(get_db_conn)
):
    pass


@classroom.post("/classrooms/new", tags=["classrooms"])
async def create_classroom(
    new_classroom: Classroom, connection: Connection = Depends(get_db_conn)
):
    pass


@classroom.delete("/classrooms/{classroom_id}", tags=["classrooms"])
async def delete_classroom(
    classroom_id: int, connection: Connection = Depends(get_db_conn)
):
    pass


@classroom.get("/search/classrooms/")
def query_classrooms_by_parameters(
    name: str | None,
) -> dict[str, Classroom | list[Classroom]]:
    classrooms = get_all_classrooms()

    if name is None:
        return classrooms

    def check_item(classroom: Classroom, connection: Connection = Depends(get_db_conn)):
        return (name is None or classroom.name == name,)

    selection = [item for item in classrooms if check_item(item)]
    return {
        "query": {"name": name},
        "selection": selection,
    }
