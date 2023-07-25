from pydantic import BaseModel


class Rating(BaseModel):
    id: int
    building_id: int
    classroom_id: int
    office_id: int
    lab_id: int
    comments: str
    rate_value: int


class RateOffice(Rating):
    id: int
    building_id: int = None
    classroom_id: int = None
    office_id: int
    lab_id: int = None
    comments: str
    rate_value: int


class RateBuilding(Rating):
    id: int
    building_id: int
    classroom_id: int = None
    office_id: int = None
    lab_id: int = None
    comments: str
    rate_value: int


class RateClassroom(Rating):
    id: int
    building_id: int = None
    classroom_id: int
    office_id: int = None
    lab_id: int = None
    comments: str
    rate_value: int


class RateLaboratory(Rating):
    id: int
    building_id: int = None
    classroom_id: int = None
    office_id: int = None
    lab_id: int
    comments: str
    rate_value: int
