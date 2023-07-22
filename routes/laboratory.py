from fastapi import APIRouter, Depends
from psycopg import Connection

from compax_api.database import get_db_conn
from schema.laboratory import Laboratory

lab = APIRouter()


@lab.get("/labs/", tags=["labs"])
async def get_all_labs(connection: Connection = Depends(get_db_conn)):
    pass


@lab.get("/labs/{lab_id}", tags=["labs"])
async def get_lab(lab_id: int, connection: Connection = Depends(get_db_conn)):
    pass


@lab.put("/labs/{lab_id}", tags=["labs"])
async def update_lab(lab_id: int, connection: Connection = Depends(get_db_conn)):
    pass


@lab.post("/labs/new", tags=["labs"])
async def create_lab(
    new_lab: Laboratory, connection: Connection = Depends(get_db_conn)
):
    pass


@lab.delete("/labs/{lab_id}", tags=["labs"])
async def delete_lab(lab_id: int, connection: Connection = Depends(get_db_conn)):
    pass


@lab.get("/search/labs/")
def query_labs_by_parameters(
    name: str | None,
) -> dict[str, Laboratory | list[Laboratory]]:
    labs = get_all_labs()

    if name is None:
        return labs

    def check_item(lab: Laboratory, connection: Connection = Depends(get_db_conn)):
        return (name is None or lab.name == name,)

    selection = [item for item in labs if check_item(item)]
    return {
        "query": {"name": name},
        "selection": selection,
    }
