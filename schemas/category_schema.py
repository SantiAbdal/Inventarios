from pydantic import BaseModel, Field
from typing import List, Optional

class CategoryBase(BaseModel):
    name: str = Field(min_length=2, max_length=100)

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2, max_length=100)

class Category(CategoryBase):    
    id: int

    class Config:
        from_attributes = True  
