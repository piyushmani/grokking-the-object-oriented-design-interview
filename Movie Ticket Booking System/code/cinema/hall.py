from dataclasses import dataclass
from typing import List
from .seat import Seat

@dataclass
class Hall:
    number: int
    seats: List[Seat]
