from Entities.Order import Order
from Infrastructure.OrderRepository import OrderRepository
import datetime

class CreateOrderUseCase:
    def __init__(self, order_repository, user_repository):
        self.order_repository = order_repository
        self.user_repository = user_repository

    def execute(self, user_id: int, product_ids: list, total_amount: float):
        order_date = datetime.datetime.utcnow()
        new_order = Order(user_id=user_id, order_date=order_date, total_amount=total_amount)
        self.order_repository.save(new_order)
        return "Order created successfully."