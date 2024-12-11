from sqlalchemy.orm import sessionmaker
from Infrastructure.OrderRepository import OrderRepository
from Entities.Order import Order
from sqlalchemy import create_engine

class OrderController:
    def __init__(self, create_order_use_case, add_to_cart_use_case):
        self.create_order_use_case = create_order_use_case
        self.add_to_cart_use_case = add_to_cart_use_case

    def create_order(self, user_email: str, product_ids: list, total_price: float):
        user = self.create_order_use_case.user_repository.find_by_email(user_email)
        if not user:
            return "User not found."
        return self.create_order_use_case.execute(user.id, product_ids, total_price)

    def add_to_cart(self, order_id: int, product_id: int, quantity: int):
        return self.add_to_cart_use_case.execute(order_id, product_id, quantity)


