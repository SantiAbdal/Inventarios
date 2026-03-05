from datetime import date
from decimal import Decimal
from schemas.product_condition_schema import ProductCondition
from category_entity import category_entity
class product_entity:
    def __init__(self, id_product:int, name:str, description: str, price : Decimal, 
                 stock: int ,stock_min: int ,condition: ProductCondition ,start_date: date,
                 category: category_entity,brand:str,cost:Decimal,sku:str):
        if not isinstance(id_product, int) or id_product <0:
            raise ValueError("id_product must be an integer")
        if not isinstance(name, str) or name == "":
            raise ValueError("name must be a string")
        if not isinstance(description, str) or description == "":
            raise ValueError("description must be a string")
        if not isinstance(price, Decimal) or price < 0:
            raise ValueError("price must be a Decimal")
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("stock must be an integer")
        if not isinstance(stock_min, int) or stock_min < 0 :
            raise ValueError("stock_min must be an integer")
        if condition not in [ProductCondition.ACTIVE, ProductCondition.DISCONTINUED,
                              ProductCondition.OUT_OF_STOCK, ProductCondition.PAUSED]:
            raise ValueError("condition must be a ProductCondition")
        if not isinstance(start_date, date) or start_date > date.today():
            raise ValueError("start_date must be a date")
        if not isinstance(category, category_entity) or category is None:
            raise ValueError("category must be a category_entity")
        if not isinstance(brand, str) or brand == "":
            raise ValueError("brand must be a string")
        if not isinstance(cost, Decimal) or cost < 0:
            raise ValueError("cost must be a Decimal")
        if not isinstance(sku, str) or sku == "":
            raise ValueError("sku must be a string")
        
        self.__id_product = id_product
        self.__name = name
        self.__description = description
        self.__price = price
        self.__stock = stock
        self.__stock_min = stock_min
        self.__condition = condition
        self.__start_date = start_date
        self.__category = category
        self.__brand = brand
        self.__cost = cost
        self.__sku = sku

    def get_id_product(self):
        return self.__id_product   
    
    def get_name(self):
        return self.__name
    
    def get_description(self):
        return self.__description
    
    def get_price(self):
        return self.__price
    
    def get_stock(self):
        return self.__stock
    
    def get_stock_min(self):
        return self.__stock_min
    
    def get_condition(self):
        return self.__condition
    
    def get_start_date(self):
        return self.__start_date
    
    def get_category(self):
        return self.__category
    
    def get_brand(self):
        return self.__brand
    
    def get_cost(self):
        return self.__cost
    
    def get_sku(self):
        return self.__sku
    