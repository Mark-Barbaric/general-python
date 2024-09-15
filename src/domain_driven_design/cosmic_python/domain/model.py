from typing import TypeVar
from dataclasses import dataclass
from typing import Optional
from datetime import date


SKU = TypeVar("SKU", bound=str)


@dataclass(frozen=True)
class OrderLine:
    order_id: str
    sku: SKU
    qty: int

    def __eq__(self, other):
        return self.order_id == other.order_id


class Batch:
    def __init__(self,
                 ref: str,
                 sku: SKU,
                 qty: int,
                 eta: Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations: set[OrderLine] = set()

    def allocate(self, line: OrderLine) -> bool:
        if self.can_allocate(line):
            self._allocations.add(line)
            return True
        else:
            return False

    def deallocate(self, line: OrderLine) -> bool:
        if line in self._allocations:
            self._allocations.remove(line)
            return True
        else:
            return False

    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty
