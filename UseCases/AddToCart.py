from Entities.Cart import Cart
from Infrastructure.CartRepository import CartRepository
from Infrastructure.OrderRepository import OrderRepository
from Infrastructure.ProductRepository import ProductRepository

class AddToCartUseCase:
    def __init__(self, cart_repository, order_repository, product_repository):
        self.cart_repository = cart_repository
        self.order_repository = order_repository
        self.product_repository = product_repository

    def execute(self, order_id: int, product_id: int, quantity: int):
        # Lấy user_id từ đơn hàng
        order = self.order_repository.find_by_id(order_id)
        if not order:
            return "Order not found."
        user_id = order.user_id

        # Tìm item trong giỏ hàng
        existing_cart_item = self.cart_repository.find_by_user_and_product(user_id, product_id)
        if existing_cart_item:
            # Cập nhật số lượng nếu item đã tồn tại
            existing_cart_item.quantity += quantity
            self.cart_repository.save(existing_cart_item)
            return "Cart item updated."
        else:
            # Thêm item mới nếu chưa tồn tại
            new_cart_item = Cart(user_id=user_id, product_id=product_id, quantity=quantity)
            self.cart_repository.save(new_cart_item)
            return "Cart item added."
