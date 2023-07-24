from fastapi import APIRouter, Depends
from psycopg import Connection

from compax_api.database import get_db_conn
import compax_api.utils
from schema.buildings import Building

building = APIRouter()


# TODO handle all errors after queries


@building.get("/buildings/", tags=["buildings"])
async def get_all_buildings(connection: Connection = Depends(get_db_conn)):
    res = compax_api.utils._get_all_and_execute("get_all_buildings.sql", connection)
    return res


@building.get("/building/{building_id}", tags=["buildings"])
async def get_building(building_id: int, connection: Connection = Depends(get_db_conn)):
    res = compax_api.utils._get_one_and_execute_params(
        "get_building_with_id.sql", {"building_id": building_id}, connection
    )
    return res


@building.get("/building/", tags=["buildings"])
async def search_building_with_name(
    name: str, connection: Connection = Depends(get_db_conn)
):
    name = f"%{name}%"
    res = compax_api.utils._get_all_and_execute_params(
        "get_building_with_name.sql", {"name": name}, connection
    )
    return res


@building.put("/buildings/{building_id}", tags=["buildings"])
async def update_building(
    building_id: int,
    new_name: str = None,
    image_url: str = None,
    connection: Connection = Depends(get_db_conn),
):
    pass


@building.patch("/building/image/{building_id}", tags=["buildings"])
async def update_building_image(
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


# @building.get("/search/buildings/")
# def query_buildings_by_parameters(
#     name: str,
# ) -> dict[str, Building | list[Building]]:
#     buildings = get_all_buildings()

#     if name is None:
#         return buildings

#     def check_item(building: Building, connection: Connection = Depends(get_db_conn)):
#         return (name is None or building.name == name,)

#     selection = [item for item in buildings if check_item(item)]
#     return {
#         "query": {"name": name},
#         "selection": selection,
#     }
