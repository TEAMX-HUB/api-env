from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    pass


class User(UserBase):
    pass
