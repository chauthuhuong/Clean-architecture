from sqlalchemy.orm import sessionmaker
from Infrastructure.ProductRepository import ProductRepository
from Entities.Product import Product
from sqlalchemy import create_engine

class ProductController:
    def __init__(self, create_product_use_case):
        self.create_product_use_case = create_product_use_case

    def create_product(self, name: str, description: str, price: float, category_id: int, stock: int) -> str:
        return self.create_product_use_case.execute(name, description, price, category_id, stock)
