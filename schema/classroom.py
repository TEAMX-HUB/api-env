from pydantic import BaseModel


class Classroom(BaseModel):
    id: int
    name: str
    image_url: str
    room_number: int | 0
    floor_number: int | 0
    goem: str
    building_id: int
