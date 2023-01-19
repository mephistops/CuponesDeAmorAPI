from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from crud import get_coupon, get_coupons, create_coupon
from models import Coupons, Base
from schemas import Coupons, CouponsCreate
from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://wondrous-cranachan-8631ca.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/coupons/", response_model=Coupons)
def read_coupon(coupon_id: int, db: Session = Depends(get_db)):
    coupon = get_coupon(db, id=coupon_id)
    return coupon


@app.get("/coupon/", response_model=list[Coupons])
def read_coupons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    coupons = get_coupons(db, skip=skip, limit=limit)
    return coupons

@app.post("/coupon/", response_model=Coupons)
def create_coupons(coupon: CouponsCreate, db: Session = Depends(get_db)):
    return create_coupon(db=db, coupon=coupon)