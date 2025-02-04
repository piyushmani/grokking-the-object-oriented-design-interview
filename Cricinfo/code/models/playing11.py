from dataclasses import dataclass
from typing import List
from .team import Team
from .player import Player

@dataclass
class Playing11:
    team: Team
    players: List[Player]

    def substitute_player(self, out_player: Player, in_player: Player):
        if out_player in self.players:
            index = self.players.index(out_player)
            self.players[index] = in_player