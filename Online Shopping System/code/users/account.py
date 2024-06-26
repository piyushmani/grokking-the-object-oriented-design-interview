from dataclasses import dataclass, field
from typing import List
from enum import Enum

class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6

@dataclass
class Address:
    street_address: str
    city: str
    state: str
    zip_code: int
    country: str

@dataclass
class Account:
    username: str
    password: str
    name: str
    email: str
    phone: str
    shipping_address: Address
    status: 'AccountStatus' = 'AccountStatus.ACTIVE'
    credit_cards: List[str] = field(default_factory=list)
    bank_accounts: List[str] = field(default_factory=list)

    def add_product(self, product):
        pass

    def add_productReview(self, review):
        pass

    def reset_password(self):
        pass
