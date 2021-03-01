from typing import Optional

from pydantic import BaseModel


class ProductIn(BaseModel):
    name: str
    category: str
    quantity: int


class Product(ProductIn):
    id: str

    class Config:
        orm_mode = True


class ProductUpdate(BaseModel):
    name: Optional[str]
    category: Optional[str]
    quantity: Optional[int]


class DeleteStatus(BaseModel):
    detail: str
