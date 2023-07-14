from pydantic import BaseModel


class RateBase(BaseModel):
    pass


# dont forget to add the rating value
class RateCreate(RateBase):
    pass


class Rate(RateBase):
    pass
