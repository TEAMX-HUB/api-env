from pydantic import BaseModel


class Laboratory(BaseModel):
    id: int
    lab_reference: str
    room_number: int | 0
    floor_number: int | 0
    image_url: str
    geom: str
    building_id: int
