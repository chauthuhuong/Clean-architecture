from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from base import Base
import datetime

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Khai báo cột user_id
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    total_amount = Column(Float, nullable=False)

    user = relationship("User", back_populates="orders")
