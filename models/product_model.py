from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from db.db import Base
from schemas.product_condition_schema import ProductCondition 
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import Date

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Numeric(precision=10, scale=2), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    stock = Column(Integer, nullable=False)
    stock_min = Column(Integer, nullable=False)
    condition = Column(SQLEnum(ProductCondition), nullable=False)
    start_date = Column(Date, nullable=False)
    cost = Column(Numeric(precision=10, scale=2), nullable=False)
    sku = Column(String, nullable=False, unique=True)
    brand = Column(String, nullable=False)

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("CategoryModel", back_populates="products")


