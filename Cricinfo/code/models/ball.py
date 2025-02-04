from dataclasses import dataclass
from typing import List, Optional
from .run import Run
from .wicket import Wicket
from .player import Player

@dataclass
class Ball:
    ball_number: int
    run: Run
    wicket: Optional[Wicket] = None
    batsman: Optional[Player] = None
    bowler: Optional[Player] = None
    commentary: str = ""
