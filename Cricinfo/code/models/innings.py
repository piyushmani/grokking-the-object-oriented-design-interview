from dataclasses import dataclass, field
from typing import List
from .team import Team
from .over import Over

@dataclass
class Innings:
    innings_id: int
    batting_team: Team
    bowling_team: Team
    overs: List[Over] = field(default_factory=list)
    total_runs: int = 0
    wickets: int = 0
    extras: int = 0

    def add_over(self, over: Over):
        self.overs.append(over)
        self.total_runs += over.runs_conceded
        self.wickets += over.wickets_taken

    def update_extras(self, extras: int):
        self.extras += extras
        self.total_runs += extras