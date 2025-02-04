from dataclasses import dataclass
from typing import Optional
from .player import Player

@dataclass
class Wicket:
    batsman: Player
    bowler: Player
    wicket_type: str
    fielder: Optional[Player] = None
    wicket_number: int = 0