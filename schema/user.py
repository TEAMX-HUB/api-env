from datetime import datetime
from uuid import uuid4 as UUID

from pydantic import BaseModel


class UserBase(BaseModel):
    id: UUID
    username: str
    student_reference: int | str
    department: str
    year_group: int
    password: str
    created_at: datetime | None
    is_classrep: bool
    is_admin: bool
    is_deleted: bool
    is_exams_officer: bool


class UserCreate(UserBase):
    is_admin: bool = False


class AdminBase(UserBase):
    pass


class AdminCreate(AdminBase):
    is_admin: bool = True
    is_exams_officer: bool = False


class ExamOfficer(UserBase):
    pass


class ExamOfficerCreate(ExamOfficer):
    is_admin: bool = True
    is_exams_officer: bool = True
