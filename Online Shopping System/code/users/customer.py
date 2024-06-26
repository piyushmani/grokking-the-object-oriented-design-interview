from dataclasses import dataclass, field
from users.account import Account

@dataclass
class Customer:
    account: Account
    cart: list = field(default_factory=list)
    order: list = field(default_factory=list)

    def add_item_to_cart(self, item):
        self.cart.append(item)

    def place_order(self, order):
        self.order.append(order)