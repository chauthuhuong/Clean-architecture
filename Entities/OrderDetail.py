from sqlalchemy import Column, String, create_engine
from base import Base
from sqlalchemy.orm import sessionmaker

class OrderDetail(Base):
    __tablename__ = "order_details"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    order = relationship("Order", back_populates="order_details")
    product = relationship("Product", back_populates="order_details")

Order.order_details = relationship("OrderDetail", back_populates="order")
Product.order_details = relationship("OrderDetail", back_populates="product")
