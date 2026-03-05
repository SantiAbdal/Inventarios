from sqlalchemy.exc import IntegrityError

from fastapi import HTTPException
from sqlalchemy.orm import Session
from repository.category_repository import CategoryRepository
from schemas.category_schema import CategoryCreate

class CategoryService:

    def __init__(self):
        self.repo = CategoryRepository()

    def get_category_by_id(self, db: Session, category_id: int):
        category = self.repo.get_category_by_id(db, category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return category

    def get_all_categories(self, db: Session):
        return self.repo.get_all_categories(db)

    def create_category(self, db: Session, category_data: CategoryCreate):
        try:
            return self.repo.create_category(db, category_data)
        except IntegrityError:
           db.rollback()
           raise HTTPException(
            status_code=400,
            detail="Category name already exists"
        )

    def get_category_by_name(self, db: Session, name: str):
        category = self.repo.get_category_by_name(db, name)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return category

    def delete_category(self, db: Session, category_id: int):
        success = self.repo.delete_category(db, category_id)
        if not success:
            raise HTTPException(status_code=404, detail="Category not found")
        return success