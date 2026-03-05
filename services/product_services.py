from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from repository.product_repository import ProductRepository
from schemas.product_schema import ProductCreate, ProductUpdate


class ProductService:

    ALLOWED_RANGE_FIELDS = {"price", "cost", "start_date"}
    ALLOWED_TEXT_FIELDS = {"name", "brand", "sku"}
    ALLOWED_EQUALITY_FIELDS = {"category_id", "condition"}

    def get_product_by_id(self, db: Session, product_id: int):
        repo = ProductRepository(db)
        product = repo.get_by_id(product_id)

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        return product

    def get_all_products(self, db: Session):
        repo = ProductRepository(db)
        return repo.get_all()

    def create_product(self, db: Session, product_data: ProductCreate):
        repo = ProductRepository(db)
        try:
            return repo.create(product_data)
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=400,
                detail="SKU already exists"
            )

    def delete_product(self, db: Session, product_id: int):
        repo = ProductRepository(db)
        success = repo.delete(product_id)

        if not success:
            raise HTTPException(status_code=404, detail="Product not found")

        return success

    def update_product(self, db: Session, product_id: int, product_update: ProductUpdate):
        repo = ProductRepository(db)
        product = repo.get_by_id(product_id)

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        update_data = product_update.model_dump(exclude_unset=True)

        new_stock = update_data.get("stock", product.stock)
        new_stock_min = update_data.get("stock_min", product.stock_min)

        if new_stock < new_stock_min:
            raise HTTPException(
                status_code=400,
                detail="Stock cannot be less than minimum stock"
            )

        for field, value in update_data.items():
            setattr(product, field, value)

        return repo.save(product)
    def search_by_text(self, db: Session, field: str, value: str):
      if field not in self.ALLOWED_TEXT_FIELDS:
         raise HTTPException(status_code=400, detail="Invalid text field")

      repo = ProductRepository(db)
      return repo.get_by_text_field(field, value)
    
    def search_by_equal(self, db: Session, field: str, value):
        if field not in self.ALLOWED_EQUALITY_FIELDS:
            raise HTTPException(status_code=400, detail="Invalid equality field")
        repo = ProductRepository(db)
        return repo.get_by_field(field, value)
    
    def search_by_range(self, db: Session, field: str, min_value, max_value):
        if field not in self.ALLOWED_RANGE_FIELDS:
            raise HTTPException(status_code=400, detail="Invalid range field")
        repo = ProductRepository(db)
        return repo.get_by_range(field, min_value, max_value)
    
    def search_by_category_name(self, db: Session, category_name: str):
        repo = ProductRepository(db)
        return repo.get_by_category_name(category_name)
    