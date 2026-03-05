from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field
from schemas.category_schema import Category
from schemas.product_condition_schema import ProductCondition


# -------------------------
# Base (campos compartidos)
# -------------------------
class ProductBase(BaseModel):
    price: Decimal = Field(gt=0)
    name: str
    brand: str
    description: str
    stock: int = Field(ge=0)
    stock_min: int = Field(ge=0)
    condition: ProductCondition
    start_date: date
    cost: Decimal = Field(ge=0)
    sku: str


# -------------------------
# Create (input para POST)
# -------------------------
class ProductCreate(ProductBase):
    category_id: int


# -------------------------
# Update (input para PATCH)
# -------------------------
class ProductUpdate(BaseModel):
    price: Optional[Decimal] = Field(default=None, gt=0)
    name: Optional[str] = None
    brand: Optional[str] = None
    description: Optional[str] = None
    stock: Optional[int] = Field(default=None, ge=0)
    stock_min: Optional[int] = Field(default=None, ge=0)
    condition: Optional[ProductCondition] = None
    start_date: Optional[date] = None
    category_id: Optional[int] = None
    cost: Optional[Decimal] = Field(default=None, ge=0)
    sku: Optional[str] = None


# -------------------------
# Response (output)
# -------------------------
class Product(ProductBase):
    id: int
    category: Category

    class Config:
        from_attributes = True  # importante si usás SQLAlchemy ORM
