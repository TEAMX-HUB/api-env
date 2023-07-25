from fastapi import APIRouter, Depends
from psycopg import Connection

from compax_api.database import get_db_conn
import compax_api.utils
from schema.office import Office

office = APIRouter()


@office.get("/offices/", tags=["offices"])
async def get_all_offices(connection: Connection = Depends(get_db_conn)):
    res = compax_api.utils._get_all_and_execute("get_all_offices.sql", connection)
    return res


@office.get("/office/{office_id}", tags=["offices"])
async def get_office(office_id: int, connection: Connection = Depends(get_db_conn)):
    res = compax_api.utils._get_one_and_execute_params(
        "get_office_with_id.sql", {"office_id": office_id}, connection
    )
    return res


@office.get("/office/", tags=["offices"])
async def search_office_with_name(
    staff_personnel: str, connection: Connection = Depends(get_db_conn)
):
    staff_personnel = f"%{staff_personnel}%"
    res = compax_api.utils._get_all_and_execute_params(
        "get_office_with_name.sql", {"staff_personnel": staff_personnel}, connection
    )
    return res


@office.put("/offices/{office_id}", tags=["offices"])
async def update_office(office_id: int, connection: Connection = Depends(get_db_conn)):
    pass


@office.patch("/office/image/{office_id}", tags=["offices"])
async def update_office_image(
    office_id: int, connection: Connection = Depends(get_db_conn)
):
    pass


@office.post("/offices/new", tags=["offices"])
async def create_office(
    new_office: Office, connection: Connection = Depends(get_db_conn)
):
    pass


@office.delete("/offices/{office_id}", tags=["offices"])
async def delete_office(office_id: int, connection: Connection = Depends(get_db_conn)):
    pass


# @office.get("/search/offices/")
# def query_offices_by_parameters(
#     staff_personnel: str | None,
# ) -> dict[str, Office | list[Office]]:
#     offices = get_all_offices()

#     if staff_personnel is None:
#         return offices

#     def check_item(office: Office, connection: Connection = Depends(get_db_conn)):
#         return (staff_personnel is None or office.staff_personnel in staff_personnel,)

#     selection = [item for item in offices if check_item(item)]
#     return {
#         "query": {"name": staff_personnel},
#         "selection": selection,
#     }
