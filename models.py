from sqlalchemy import Column, Integer, String

from database import Base


class Coupons(Base):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    description = Column(String)
    iconOne = Column(String)
    iconTwo = Column(String)