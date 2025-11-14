from typing import Optional

from pydantic import BaseModel


class Pizza(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    category_id: Optional[int] = None