from pydantic import BaseModel


class Office(BaseModel):
    id: int
    floor_number: int | 0
    image_url: str
    geom: str
    building_id: int
    office_code: str
    staff_personnel: str
