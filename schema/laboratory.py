from pydantic import BaseModel


class Laboratory(BaseModel):
    id: int
    lab_reference: str
    room_number: int
    floor_number: int
    image_url: list[str]
    geom: str
    building_id: int
