from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    user_id: int
    username: str
    email: str
    phone: str
    preferences: Optional[dict] = None

    def update_preferences(self, preferences: dict):
        self.preferences = preferences
