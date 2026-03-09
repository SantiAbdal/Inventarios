from pydantic import BaseModel, ConfigDict
from datetime import datetime

class StockMovementResponse(BaseModel):
    id: int
    product_id: int
    movement_type: str
    quantity: int
    created_at: datetime

    class Config:
        model_config = ConfigDict(from_attributes=True)