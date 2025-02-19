from pydantic import BaseModel, UUID4
from ..product.entities import ProductEntity
from .entities import OrderStatus

class OrderEntity(BaseModel):
    order_id: UUID4
    user_id: UUID4
    products: list[ProductEntity]
    order_status: OrderStatus
