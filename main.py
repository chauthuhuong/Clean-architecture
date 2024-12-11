from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Infrastructure.CartRepository import CartRepository
from Infrastructure.UserRepository import UserRepository
from Infrastructure.ProductRepository import ProductRepository
from Infrastructure.OrderRepository import OrderRepository
from UseCases.CreateUser import CreateUserUseCase
from UseCases.CreateProduct import CreateProductUseCase
from UseCases.CreateOrder import CreateOrderUseCase
from UseCases.AddToCart import AddToCartUseCase
from Controllers.UserController import UserController
from Controllers.ProductController import ProductController
from Controllers.OrderController import OrderController
from base import Base

engine = create_engine('mssql+pyodbc://sa:123@localhost/TestORM?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes')
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

def main():
    engine = create_engine(
        'mssql+pyodbc://sa:123@localhost/TestORM?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes'
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Tạo repository
    user_repository = UserRepository(session)
    product_repository = ProductRepository(session)
    order_repository = OrderRepository(session)
    cart_repository = CartRepository(session) 

    # Tạo use case
    create_user_use_case = CreateUserUseCase(user_repository)
    create_product_use_case = CreateProductUseCase(product_repository)
    create_order_use_case = CreateOrderUseCase(order_repository, user_repository)
    add_to_cart_use_case = AddToCartUseCase(cart_repository ,order_repository, product_repository)

    # Tạo controller
    user_controller = UserController(create_user_use_case)
    product_controller = ProductController(create_product_use_case)
    order_controller = OrderController(create_order_use_case, add_to_cart_use_case)

    # Gọi controller để tạo người dùng
    print(user_controller.create_user("test@example.com", "password123"))  # User created successfully.
    print(user_controller.create_user("test@example.com", "password456"))  # User with this email already exists.

    print(product_controller.create_product("Laptop", "High-performance laptop", 1500.0, 1, 10))  
    print(product_controller.create_product("Smartphone", "Latest model smartphone", 900.0, 2, 20))

    print(order_controller.create_order("test@example.com", [1, 2], 2400.0))  # Tạo đơn hàng với danh sách sản phẩm.

    print(order_controller.add_to_cart(order_id=1, product_id=2, quantity=3))  # Thêm sản phẩm vào đơn hàng.

if __name__ == "__main__":
    main()
