from dataclasses import dataclass, field
from orders.order_item import OrderItem
from typing import List

@dataclass
class Cart:
    items: List[OrderItem] = field(default_factory=list)

    def add_item(self, item: OrderItem):
        self.items.append(item)

    def remove_item(self, item: OrderItem):
        self.items.remove(item)
