from dataclasses import dataclass
from typing import Optional
from datetime import date
from ..value_objects import SKU


@dataclass(unsafe_hash=True)
class OrderLine:
    order_id: str
    sku: SKU
    qty: int

    def __eq__(self, other):
        return self.order_id == other.order_id