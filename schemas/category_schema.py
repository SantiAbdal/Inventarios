from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional

class CategoryBase(BaseModel):
    name: str = Field(min_length=2, max_length=100)

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2, max_length=100)

class Category(CategoryBase):    
    id: int

    model_config = ConfigDict(from_attributes=True)
