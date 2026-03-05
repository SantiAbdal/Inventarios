from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.db import Base
class CategoryModel(Base):
    __tablename__= "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    products = relationship("ProductModel", back_populates="category", 
                            cascade="all, delete-orphan")
    