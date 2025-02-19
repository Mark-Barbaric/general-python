from enum import Enum
from pydantic import BaseModel, UUID4


class ProductDepartment(str, Enum):
    food = "food"
    clothes = "clothes"


class ProductEntity(BaseModel):
    sku: UUID4
    department: ProductDepartment


class ClothesProductEntity(ProductEntity):
    size: str
    color: str