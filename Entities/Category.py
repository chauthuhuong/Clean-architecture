from sqlalchemy import Column, String, create_engine
from base import Base
from sqlalchemy.orm import sessionmaker

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), nullable=True)