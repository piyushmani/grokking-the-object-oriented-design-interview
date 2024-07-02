# enums/account_status.py
from enum import Enum

class AccountStatus(Enum):
    ACTIVE = 1
    CLOSED = 2
    CANCELED = 3
    BLACKLISTED = 4
    BLOCKED = 5
