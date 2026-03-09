from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.db import Base
from schemas.movement_type_schema import MovementType
from sqlalchemy import Enum as SQLEnum

class StockMovement(Base):
    __tablename__ = "stock_movements"

    id = Column(Integer, primary_key=True, index=True)

    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    movement_type = Column(String, nullable=False)  

    quantity = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    product = relationship("ProductModel")

    movement_type = Column(SQLEnum(MovementType), nullable=False)