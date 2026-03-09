from sqlalchemy.orm import Session
from models.stock_movement_model import StockMovement
from schemas.movement_type_schema import MovementType


class StockMovementRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, product_id: int, movement_type: MovementType, quantity: int):
        movement = StockMovement(
            product_id=product_id,
            movement_type=movement_type,
            quantity=quantity
        )

        self.db.add(movement)
        self.db.commit()
        self.db.refresh(movement)

        return movement

    def get_by_product(self, product_id: int):
        return (
            self.db.query(StockMovement)
            .filter(StockMovement.product_id == product_id)
            .all()
        )