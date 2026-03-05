from sqlalchemy.orm import Session
from models.product_model import ProductModel
from models.category_model import CategoryModel
from schemas.product_schema import ProductCreate


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    # ---------------------------
    # Básicos
    # ---------------------------

    def get_all(self) -> list[ProductModel]:
        return self.db.query(ProductModel).all()

    def get_by_id(self, product_id: int) -> ProductModel | None:
        return (
            self.db.query(ProductModel)
            .filter(ProductModel.id == product_id)
            .first()
        )

    def create(self, product_data: ProductCreate) -> ProductModel:
        product = ProductModel(**product_data.model_dump())
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete(self, product_id: int) -> bool:
        product = self.get_by_id(product_id)
        if not product:
            return False

        self.db.delete(product)
        self.db.commit()
        return True

    def save(self, product: ProductModel) -> ProductModel:
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    # ---------------------------
    # Búsquedas dinámicas
    # ---------------------------

    def get_by_text_field(self, field: str, value: str) -> list[ProductModel]:
        column = getattr(ProductModel, field)
        return (
            self.db.query(ProductModel)
            .filter(column.ilike(f"%{value}%"))
            .all()
        )

    def get_by_field(self, field: str, value) -> list[ProductModel]:
        column = getattr(ProductModel, field)
        return (
            self.db.query(ProductModel)
            .filter(column == value)
            .all()
        )

    def get_by_range(self, field: str, min_value, max_value) -> list[ProductModel]:
        column = getattr(ProductModel, field)
        query = self.db.query(ProductModel)

        if min_value is not None:
            query = query.filter(column >= min_value)

        if max_value is not None:
            query = query.filter(column <= max_value)

        return query.all()

    def get_by_category_name(self, category_name: str) -> list[ProductModel]:
        return (
            self.db.query(ProductModel)
            .join(CategoryModel)
            .filter(CategoryModel.name == category_name)
            .all()
        )
    
    
    