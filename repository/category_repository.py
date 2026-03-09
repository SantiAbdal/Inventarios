from sqlalchemy.orm import Session
from schemas.category_schema import CategoryCreate
from models.category_model import CategoryModel

class CategoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, category: CategoryCreate) -> CategoryModel:
        db_category = CategoryModel(name=category.name)
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def get_by_id(self, category_id: int) -> CategoryModel | None:
        return self.db.query(CategoryModel).filter(CategoryModel.id == category_id).first()

    def get_all(self) -> list[CategoryModel]:
        return self.db.query(CategoryModel).all()

    def get_by_name(self, name: str) -> CategoryModel | None:
        return self.db.query(CategoryModel).filter(CategoryModel.name == name).first()

    def delete(self, category_id: int) -> bool:
        category = self.get_by_id(category_id)
        if not category:
            return False
        self.db.delete(category)
        self.db.commit()
        return True

    def save(self, category: CategoryModel) -> CategoryModel:
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category