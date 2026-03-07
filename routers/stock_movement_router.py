from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.db import SessionLocal
from services.product_services import ProductService

router = APIRouter(prefix="/stock", tags=["Stock"])

service = ProductService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/in/{sku}")
def increase_stock(sku: str, quantity: int, db: Session = Depends(get_db)):
    return service.increase_stock(db, sku, quantity)


@router.post("/out/{sku}")
def reduce_stock(sku: str, quantity: int, db: Session = Depends(get_db)):
    return service.reduce_stock(db, sku, quantity)