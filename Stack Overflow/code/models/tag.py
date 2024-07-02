# models/tag.py
from dataclasses import dataclass

@dataclass
class Tag:
    name: str
    description: str
    daily_asked_frequency: int = 0
    weekly_asked_frequency: int = 0
