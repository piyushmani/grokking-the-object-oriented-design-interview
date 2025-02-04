from dataclasses import dataclass, field
from typing import List, Optional
from .ball import Ball
from .player import Player

@dataclass
class Over:
    over_number: int
    balls: List[Ball] = field(default_factory=list)
    bowler: Optional[Player] = None
    runs_conceded: int = 0
    wickets_taken: int = 0

    def add_ball(self, ball: Ball):
        self.balls.append(ball)
        self.runs_conceded += ball.run.runs + ball.run.extras
        if ball.wicket:
            self.wickets_taken += 1