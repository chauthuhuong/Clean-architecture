from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Định nghĩa cột user_id
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    user = relationship("User", back_populates="carts")
    product = relationship("Product", back_populates="carts")
