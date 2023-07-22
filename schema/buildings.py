from pydantic import BaseModel


class Building(BaseModel):
    id: int
    name: str
    image_url: list[str]
    goem: str
    building_id: int
    building_type: str
    n_floors: int
    n_classrooms: int
    n_labs: int
