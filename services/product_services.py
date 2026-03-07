from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from repository.product_repository import ProductRepository
from schemas.product_schema import ProductCreate, ProductUpdate
from repository.stock_movement_repository import StockMovementRepository

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
            raise HTTPException(status_code=400,detail="SKU already exists")

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

        if new_stock < 0:
            raise HTTPException(status_code=400,detail="Stock cannot be negative")

        if new_stock < new_stock_min:
            raise HTTPException(status_code=400,detail="Stock cannot be less than minimum stock")

        for field, value in update_data.items():
            setattr(product, field, value)

        return repo.save(product)

    # ---------------------------
    # Búsquedas
    # ---------------------------

    def search_by_text(self, db: Session, field: str, value: str):

        if field not in self.ALLOWED_TEXT_FIELDS:
            raise HTTPException(status_code=400, detail="Invalid text field")

        repo = ProductRepository(db)
        products = repo.get_by_text_field(field, value)

        if not products:
            raise HTTPException(status_code=404, detail="No products found")

        return products

    def search_by_equal(self, db: Session, field: str, value):

        if field not in self.ALLOWED_EQUALITY_FIELDS:
            raise HTTPException(status_code=400, detail="Invalid equality field")

        repo = ProductRepository(db)
        products = repo.get_by_field(field, value)

        if not products:
            raise HTTPException(status_code=404, detail="No products found")

        return products

    def search_by_range(self, db: Session, field: str, min_value, max_value):

        if field not in self.ALLOWED_RANGE_FIELDS:
            raise HTTPException(status_code=400, detail="Invalid range field")

        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise HTTPException(status_code=400,detail="min_value cannot be greater than max_value")

        repo = ProductRepository(db)
        products = repo.get_by_range(field, min_value, max_value)

        if not products:
            raise HTTPException(status_code=404, detail="No products found")

        return products

    def search_by_category_name(self, db: Session, category_name: str):

        repo = ProductRepository(db)
        products = repo.get_by_category_name(category_name)

        if not products:
            raise HTTPException(status_code=404, detail="No products found")

        return products

    # ---------------------------
    # Stock
    # ---------------------------

    def reduce_stock(self, db: Session, sku: str, quantity: int):

        if quantity <= 0:
            raise HTTPException(status_code=400,detail="Quantity must be greater than zero")
        movement_repo = StockMovementRepository(db)
        product_repo = ProductRepository(db)
        product = product_repo.get_by_sku(sku)

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        if product.stock < quantity:
            raise HTTPException(status_code=400,detail="Insufficient stock")

        product.stock -= quantity
        movement_repo.create(product_id=product.id,movement_type="OUT",quantity=quantity)

        if product.stock < 0:
            raise HTTPException(status_code=400,detail="Stock cannot be negative")

        return product_repo.save(product)

    def increase_stock(self, db: Session, sku: str, quantity: int):

        if quantity <= 0:
            raise HTTPException(status_code=400,detail="Quantity must be greater than zero")

        product_repo = ProductRepository(db)
        movement_repo = StockMovementRepository(db)
        product = product_repo.get_by_sku(sku)

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        product.stock += quantity
        movement_repo.create(product_id=product.id,movement_type="IN",quantity=quantity)
        return product_repo.save(product)
   
    def get_low_stock_products(self, db: Session):
        repo = ProductRepository(db)
        return repo.get_low_stock()