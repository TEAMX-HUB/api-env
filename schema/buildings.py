from pydantic import BaseModel


class Building(BaseModel):
    id: int
    name: str
    image_url: str
    goem: str
    building_id: int
    building_type: str
    n_floors: int | 0
    n_classrooms: int | 0
    n_labs: int | 0
