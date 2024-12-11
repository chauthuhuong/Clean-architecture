from Entities.Product import Product
from Infrastructure.ProductRepository import ProductRepository

class CreateProductUseCase:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def execute(self, name: str, description: str, price: float, category_id: int, stock: int) -> str:
        existing_product = self.product_repository.find_by_name(name)
        if existing_product:
            return "Product already exists."

        new_product = Product(name=name, description=description, price=price, category_id=category_id, stock=stock)
        self.product_repository.save(new_product)
        return "Product created successfully."