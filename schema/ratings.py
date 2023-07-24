from uuid import uuid4 as UUID

from pydantic import BaseModel


class Rating(BaseModel):
    id: int
    user_id: UUID
    building_id: int
    classroom_id: int
    office_id: int
    lab_id: int
    comments: str
    rate_value: int
