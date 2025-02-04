from dataclasses import dataclass
from typing import List
from .match import Match
from .innings import Innings

@dataclass
class Scorecard:
    scorecard_id: int
    match: Match
    innings: List[Innings]

    def add_innings(self, innings: Innings):
        self.innings.append(innings)

    def get_match_summary(self) -> str:
        summary_parts = []
        for i, inn in enumerate(self.innings, start=1):
            summary_parts.append(
                f"Innings {i}: {inn.batting_team.name} "
                f"scored {inn.total_runs}/{inn.wickets} in {len(inn.overs)} overs"
            )
        return " | ".join(summary_parts)