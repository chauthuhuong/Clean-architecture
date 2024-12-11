from sqlalchemy.orm import sessionmaker
from Entities.Cart import Cart
from sqlalchemy import create_engine

class CartRepository:
    def __init__(self, session):
        self.session = session

    def add_to_cart(self, user_email, product_id):
        cart = Cart(user_email=user_email, product_id=product_id)
        self.session.add(cart)
        self.session.commit()

    def get_cart_items(self, user_email):
        return self.session.query(Cart).filter_by(user_email=user_email).all()
    

    def find_by_user_and_product(self, user_id: int, product_id: int):
        return self.session.query(Cart).filter_by(user_id=user_id, product_id=product_id).first()

    def save(self, cart_item):
        self.session.add(cart_item)
        self.session.commit()
