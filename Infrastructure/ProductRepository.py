from Entities.Product import Product

class ProductRepository:
    def __init__(self, session):
        self.session = session

    def save(self, product: Product):
        self.session.add(product)
        self.session.commit()

    def find_by_name(self, name: str):
        return self.session.query(Product).filter_by(name=name).first()

    def get_all(self):
        return self.session.query(Product).all()

    def update_stock(self, product_id: int, new_stock: int):
        product = self.session.query(Product).filter_by(id=product_id).first()
        if product:
            product.stock_quantity = new_stock
            self.session.commit()

    def delete(self, product_id: int):
        product = self.session.query(Product).filter_by(id=product_id).first()
        if product:
            self.session.delete(product)
            self.session.commit()