from .alllocations import allocation_route
from .base import base_route

route_blueprints = {
    'base': base_route, 
    'allocations': allocation_route
}