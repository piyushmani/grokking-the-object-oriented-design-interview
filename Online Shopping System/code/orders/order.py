from dataclasses import dataclass, field
from typing import List
from enum import Enum
from orders.order_item import OrderItem

class OrderStatus(Enum):
    UNSHIPPED, PENDING, SHIPPED, COMPLETED, CANCELED, REFUND_APPLIED = 1, 2, 3, 4, 5, 6

@dataclass
class Order:
    order_id: int
    customer_id: int
    order_items: list[OrderItem] = field(default_factory=list)
