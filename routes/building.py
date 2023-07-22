from fastapi import APIRouter, Depends
from psycopg import Connection

from compax_api.database import get_db_conn
from schema.buildings import Building

building = APIRouter()


@building.get("/buildings/", tags=["buildings"])
async def get_all_buildings(connection: Connection = Depends(get_db_conn)):
    pass


@building.get("/buildings/{building_id}", tags=["buildings"])
async def get_building(building_id: int, connection: Connection = Depends(get_db_conn)):
    pass


@building.put("/buildings/{building_id}", tags=["buildings"])
async def update_building(
    building_id: int, connection: Connection = Depends(get_db_conn)
):
    pass


@building.post("/buildings/new", tags=["buildings"])
async def create_building(
    new_building: Building, connection: Connection = Depends(get_db_conn)
):
    pass


@building.delete("/buildings/{building_id}", tags=["buildings"])
async def delete_building(
    building_id: int, connection: Connection = Depends(get_db_conn)
):
    pass


@building.get("/search/buildings/")
def query_buildings_by_parameters(
    name: str | None,
) -> dict[str, Building | list[Building]]:
    buildings = get_all_buildings()

    if name is None:
        return buildings

    def check_item(building: Building, connection: Connection = Depends(get_db_conn)):
        return (name is None or building.name == name,)

    selection = [item for item in buildings if check_item(item)]
    return {
        "query": {"name": name},
        "selection": selection,
    }
