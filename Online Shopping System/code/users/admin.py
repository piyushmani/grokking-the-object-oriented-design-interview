from dataclasses import dataclass
from users.account import Account

@dataclass
class Admin:
    account: Account

    def add_product(self, product):
        pass

    def remove_product(self, product_id):
        pass
