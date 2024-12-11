from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)  
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = self._hash_password(password)

    def _hash_password(self, password: str) -> str:
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()

    carts = relationship("Cart", back_populates="user")
    orders = relationship("Order", back_populates="user")



