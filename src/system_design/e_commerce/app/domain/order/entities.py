from enum import Enum


class OrderStatus(str, Enum):
    processing = "processing"
    in_progress = "in_progress"
    processed = "processed"
    out_for_delivery = "out_for_delivery"
    cancelled = "cancelled"
