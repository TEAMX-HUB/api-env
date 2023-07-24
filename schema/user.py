from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UserBase(BaseModel):
    id: UUID
    username: str
    student_reference: int
    department: str
    year_group: int
    password: str
    created_at: datetime
    is_classrep: bool
    is_admin: bool
    is_deleted: bool
    is_exams_officer: bool


class UserCreate(UserBase):
    is_classrep: bool = False
    is_admin: bool = False
    is_deleted: bool = False
    is_exams_officer: bool = False


class AdminBase(UserBase):
    pass


class AdminCreate(AdminBase):
    is_classrep: bool = False
    is_admin: bool = True
    is_deleted: bool = False
    is_exams_officer: bool = False


class ExamOfficer(UserBase):
    pass


class ExamOfficerCreate(ExamOfficer):
    is_classrep: bool = False
    is_admin: bool = True
    is_exams_officer: bool = True
    is_deleted: bool = False
