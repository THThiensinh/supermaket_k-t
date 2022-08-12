from pydantic import BaseModel


class BuyItem(BaseModel):
    name: str
    bulk: int
    total: float


class Cart(BaseModel):
    total: float
    items: list[BuyItem]
