from pydantic import BaseModel


class Classroom(BaseModel):
    id: int
    name: str
    image_url: list[str]
    room_number: int
    floor_number: int
    goem: str
    building_id: int
