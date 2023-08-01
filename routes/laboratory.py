from fastapi import APIRouter, Depends
from psycopg import Connection

from compax_api.database import get_db_conn
import compax_api.utils
from schema.laboratory import Laboratory

lab = APIRouter()


@lab.get("/labs/", tags=["labs"])
async def get_all_labs(connection: Connection = Depends(get_db_conn)):
    res = compax_api.utils._get_all_and_execute("get_all_labs.sql", connection)
    return res


@lab.get("/lab/{lab_id}", tags=["labs"])
async def get_lab(lab_id: int, connection: Connection = Depends(get_db_conn)):
    res = compax_api.utils._get_one_and_execute_params(
        "get_lab_with_id.sql", {"lab_id": lab_id}, connection
    )
    return res


@lab.get("/search/labs/", tags=["labs"])
async def search_lab_with_name(
    lab_reference: str, connection: Connection = Depends(get_db_conn)
):
    name = f"%{lab_reference}%"
    res = compax_api.utils._get_all_and_execute_params(
        "get_lab_with_name.sql", {"name": name}, connection
    )
    return res


@lab.put("/labs/{lab_id}", tags=["labs"])
async def update_lab(lab_id: int, connection: Connection = Depends(get_db_conn)):
    pass


@lab.patch("/labs/image/{lab_id}", tags=["labs"])
async def update_lab_image(lab_id: int, connection: Connection = Depends(get_db_conn)):
    pass


@lab.post("/labs/new", tags=["labs"])
async def create_lab(
    new_lab: Laboratory, connection: Connection = Depends(get_db_conn)
):
    pass


@lab.delete("/labs/{lab_id}", tags=["labs"])
async def delete_lab(lab_id: int, connection: Connection = Depends(get_db_conn)):
    pass


# @lab.get("/search/labs/")
# def query_labs_by_parameters(
#     name: str | None,
# ) -> dict[str, Laboratory | list[Laboratory]]:
#     labs = get_all_labs()

#     if name is None:
#         return labs

#     def check_item(lab: Laboratory, connection: Connection = Depends(get_db_conn)):
#         return (name is None or lab.name == name,)

#     selection = [item for item in labs if check_item(item)]
#     return {
#         "query": {"name": name},
#         "selection": selection,
#     }
