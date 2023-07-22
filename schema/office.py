from pydantic import BaseModel


class Office(BaseModel):
    id: int
    floor_number: int
    image_url: list[str]
    geom: str
    building_id: int
    office_code: str
    staff_personnel: str
