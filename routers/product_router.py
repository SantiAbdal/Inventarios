from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import SessionLocal

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db import SessionLocal
from services.product_services import ProductService
from schemas.product_schema import ProductCreate, ProductUpdate, Product

router = APIRouter(prefix="/products", tags=["Products"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    service = ProductService()
    return service.get_product_by_id(db, product_id)


@router.get("", response_model=list[Product])
def get_all_products(db: Session = Depends(get_db)):
    service = ProductService()
    return service.get_all_products(db)


@router.post("", response_model=Product, status_code=201)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    service = ProductService()
    return service.create_product(db, product)


@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db)):
    service = ProductService()
    return service.update_product(db, product_id, product_update)


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    service = ProductService()
    service.delete_product(db, product_id)
    return {"detail": "Product deleted successfully"}

@router.get("/search/text", response_model=list[Product])
def search_by_text(field: str,value: str,db: Session = Depends(get_db)):
    service = ProductService()
    return service.search_by_text(db, field, value)

@router.get("/search/equal", response_model=list[Product])
def search_by_equal(field: str, value, db: Session = Depends(get_db)):
    service = ProductService()
    return service.search_by_equal(db, field, value)

@router.get("/search/range", response_model=list[Product])
def search_by_range(field: str, min_value: float | None, max_value: float | None, db: Session = Depends(get_db)):
    service = ProductService()
    return service.search_by_range(db, field, min_value, max_value)

@router.get("/search/category", response_model=list[Product])
def search_by_category_name(category_name: str,db: Session = Depends(get_db)):
    service = ProductService()
    return service.search_by_category_name(db, category_name)
