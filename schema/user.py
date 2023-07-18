from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    pass


class User(UserBase):
    pass


class AdminBase(UserBase):
    pass


class AdminCreate(AdminBase):
    pass


class Admin(AdminBase):
    pass


class ExamOfficer(UserBase):
    pass


class ExamOfficerCreate(ExamOfficer):
    pass


class ExamOfficer(ExamOfficer):
    pass
