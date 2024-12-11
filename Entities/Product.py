from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from base import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    category_id = Column(Integer, nullable=False) 
    
    carts = relationship("Cart", back_populates="product")
