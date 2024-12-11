from sqlalchemy import Column, String, create_engine
from base import Base
from sqlalchemy.orm import sessionmaker

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    payment_method = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)

    order = relationship("Order", back_populates="payments")

Order.payments = relationship("Payment", back_populates="order")