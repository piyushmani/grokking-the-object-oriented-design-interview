# models/bounty.py
from dataclasses import dataclass
import datetime

@dataclass
class Bounty:
    reputation: int
    expiry: datetime.datetime

    def modify_reputation(self, reputation: int):
        print(f"Bounty reputation changed from {self.reputation} to {reputation}.")
        self.reputation = reputation
