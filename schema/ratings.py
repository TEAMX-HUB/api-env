from uuid import uuid4 as UUID

from pydantic import BaseModel


class Rating(BaseModel):
    id: int
    user_id: UUID
    building_id: int | None
    classroom_id: int | None
    office_id: int | None
    lab_id: int | None
    comments: str
    rate_value: int
