from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from repository.category_repository import CategoryRepository
from schemas.category_schema import CategoryCreate

class CategoryService:

    def get_category_by_id(self, db: Session, category_id: int):
        repo = CategoryRepository(db)
        category = repo.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return category

    def get_all_categories(self, db: Session):
        repo = CategoryRepository(db)
        return repo.get_all()

    def create_category(self, db: Session, category_data: CategoryCreate):
        repo = CategoryRepository(db)
        try:
            return repo.create(category_data)
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Category name already exists")

    def get_category_by_name(self, db: Session, name: str):
        repo = CategoryRepository(db)
        category = repo.get_by_name(name)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return category

    def delete_category(self, db: Session, category_id: int):
        repo = CategoryRepository(db)
        success = repo.delete(category_id)
        if not success:
            raise HTTPException(status_code=404, detail="Category not found")
        return success