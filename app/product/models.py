from sqlalchemy import Column, Integer, String

from app.database import Base


class Product(Base):
    __tablename__ = 'products'
    internal_id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    id = Column('ext_id', String(60), unique=True, nullable=False)
    name = Column('name', String(120), nullable=False)
    category = Column('category', String(120), nullable=False)
    quantity = Column('quantity', Integer, nullable=True)