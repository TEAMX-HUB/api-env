from fastapi import APIRouter, Depends
from psycopg import Connection

from compax_api.database import get_db_conn
from schema.office import Office

office = APIRouter()


@office.get("/offices/", tags=["offices"])
async def get_all_offices(connection: Connection = Depends(get_db_conn)):
    pass


@office.get("/offices/{office_id}", tags=["offices"])
async def get_office(office_id: int, connection: Connection = Depends(get_db_conn)):
    pass


@office.put("/offices/{office_id}", tags=["offices"])
async def update_office(office_id: int, connection: Connection = Depends(get_db_conn)):
    pass


@office.post("/offices/new", tags=["offices"])
async def create_office(
    new_office: Office, connection: Connection = Depends(get_db_conn)
):
    pass


@office.delete("/offices/{office_id}", tags=["offices"])
async def delete_office(office_id: int, connection: Connection = Depends(get_db_conn)):
    pass


@office.get("/search/offices/")
def query_offices_by_parameters(
    name: str | None,
) -> dict[str, Office | list[Office]]:
    offices = get_all_offices()

    if name is None:
        return offices

    def check_item(office: Office, connection: Connection = Depends(get_db_conn)):
        return (name is None or office.name == name,)

    selection = [item for item in offices if check_item(item)]
    return {
        "query": {"name": name},
        "selection": selection,
    }
