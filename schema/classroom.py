from pydantic import BaseModel


class ClassroomBase(BaseModel):
    pass


class ClassroomCreate(ClassroomBase):
    pass


class Classroom(ClassroomBase):
    pass
