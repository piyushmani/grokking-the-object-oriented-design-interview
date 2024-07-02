# models/account.py
from dataclasses import dataclass
from enums.account_status import AccountStatus

@dataclass
class Account:
    id: str
    password: str
    name: str
    email: str
    address: str
    phone: int
    status: AccountStatus
    reputation: int = 0

    def reset_password(self, new_password: str):
        print(f"Password for account {self.id} reset to {new_password}.")
        self.password = new_password
