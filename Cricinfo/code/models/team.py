from dataclasses import dataclass
from typing import List, Optional

from .player import Player

@dataclass
class Team:
    team_id: int
    name: str
    short_name: str
    flag_url: str
    players: Optional[List[Player]] = None

    def add_player(self, player: Player):
        if self.players is None:
            self.players = []
        self.players.append(player)

    def remove_player(self, player: Player):
        if self.players and player in self.players:
            self.players.remove(player)


@dataclass
class TeamStat:
    team: Team
    matches_played: int
    matches_won: int
    matches_lost: int
    matches_drawn: int
    points: int
    net_run_rate: float

    def update_stats(self, result: str, run_rate_change: float):
        self.matches_played += 1
        if result == "won":
            self.matches_won += 1
            self.points += 2
        elif result == "lost":
            self.matches_lost += 1
        elif result == "drawn":
            self.matches_drawn += 1
            self.points += 1
        self.net_run_rate += run_rate_change
