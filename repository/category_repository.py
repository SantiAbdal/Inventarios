from sqlalchemy.orm import Session
from schemas.category_schema import CategoryCreate
from models.category_model import CategoryModel
class CategoryRepository:
    def create_category(self ,db: Session, category: CategoryCreate) -> CategoryModel:
        db_category = CategoryModel(name=category.name)
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category
    def get_category_by_id(self, db: Session, category_id: int) -> CategoryModel:
        return db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    
    def get_all_categories(self, db: Session) -> list[CategoryModel]:
        return db.query(CategoryModel).all()
    
    def get_category_by_name(self, db: Session, name: str) -> CategoryModel:
        return db.query(CategoryModel).filter(CategoryModel.name == name).first()
    
    def delete_category(self, db: Session, category_id: int) -> bool:
        db_category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
        if db_category:
            db.delete(db_category)
            db.commit()
            return True
        return False
    
    def save(self, db: Session, category: CategoryModel) -> CategoryModel:
        db.add(category)
        db.commit()
        db.refresh(category)
        return category
    