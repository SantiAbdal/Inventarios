from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.product_services import ProductService
from schemas.stock_movement_schemas import StockMovementResponse
from db.dependencies import get_db

router = APIRouter(prefix="/stock", tags=["Stock"])

service = ProductService()

@router.post("/in/{sku}")
def increase_stock(sku: str, quantity: int, db: Session = Depends(get_db)):
    return service.increase_stock(db, sku, quantity)

@router.post("/out/{sku}")
def reduce_stock(sku: str, quantity: int, db: Session = Depends(get_db)):
    return service.reduce_stock(db, sku, quantity)

@router.get("/history/{sku}", response_model=list[StockMovementResponse])
def get_stock_history(sku: str, db: Session = Depends(get_db)):
    return service.get_stock_history(db, sku)