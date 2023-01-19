from sqlalchemy.orm import Session

from models import Coupons
from schemas import CouponsCreate


def get_coupon(db: Session, id: int):
    return db.query(Coupons).filter(Coupons.id == id).first()

def get_coupons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Coupons).offset(skip).limit(limit).all()

def create_coupon(db: Session, coupon: CouponsCreate):
    db_coupon = Coupons(
        text=coupon.text,
        description=coupon.description,
        iconOne=coupon.iconOne,
        iconTwo=coupon.iconTwo,
    )
    db.add(db_coupon)
    db.commit()
    db.refresh(db_coupon)
    return db_coupon
