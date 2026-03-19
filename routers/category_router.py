from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.category_services import CategoryService
from schemas.category_schema import CategoryCreate, CategoryUpdate, Category
from db.dependencies import get_db , get_current_user
router = APIRouter(prefix="/categories", tags=["Categories"])
category_service: CategoryService = CategoryService()

## Obtener categoria por ID
@router.get("/{category_id}", response_model=Category)
def get_category(category_id: int, db: Session = Depends(get_db)):
     return category_service.get_category_by_id(db, category_id)

## Obtener todas las categorias
@router.get("/", response_model=list[Category])
def get_all_categories(db: Session = Depends(get_db)):
    return category_service.get_all_categories(db)

## Crear una nueva categoria
@router.post("/", response_model=Category, status_code=201)
def create_category(category: CategoryCreate, db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    return category_service.create_category(db, category)

# borrar una categoria
@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    category_service.delete_category(db, category_id)
    return {"detail": "Category deleted successfully"}