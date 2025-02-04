from dataclasses import dataclass
from typing import Optional

@dataclass
class Player:
    player_id: int
    name: str
    role: str
    batting_style: str
    bowling_style: str
    date_of_birth: Optional[str] = None
    nationality: Optional[str] = None

class PlayerMatchStats:
    def __init__(self, player: Player):
        self.player = player
        self.runs_scored = 0
        self.balls_faced = 0
        self.wickets_taken = 0
        self.balls_bowled = 0
        self.runs_conceded = 0
        self.catches = 0
        self.stumpings = 0

    def update(
        self,
        runs=0,
        balls_faced=0,
        wickets=0,
        balls_bowled=0,
        runs_conceded=0,
        catches=0,
        stumpings=0
    ):
        self.runs_scored += runs
        self.balls_faced += balls_faced
        self.wickets_taken += wickets
        self.balls_bowled += balls_bowled
        self.runs_conceded += runs_conceded
        self.catches += catches
        self.stumpings += stumpings

    def display(self):
        print(f"Match Statistics for {self.player.name}:")
        print(f"Runs: {self.runs_scored} ({self.balls_faced} balls)")
        print(f"Wickets: {self.wickets_taken}")
        overs_bowled = self.balls_bowled // 6
        remainder_balls = self.balls_bowled % 6
        print(f"Bowling: {self.wickets_taken}/{self.runs_conceded} in {overs_bowled}.{remainder_balls} overs")
        print(f"Catches: {self.catches}, Stumpings: {self.stumpings}")
