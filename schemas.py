from pydantic import BaseModel


class CouponsBase(BaseModel):
    text: str
    description: str
    iconOne: str
    iconTwo: str


class CouponsCreate(CouponsBase):
    pass


class Coupons(CouponsBase):
    id: int

    class Config:
        orm_mode = True
