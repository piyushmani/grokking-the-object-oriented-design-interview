from dataclasses import dataclass
from typing import List, Optional
from .match import Match
from .team import Team
from .schedule import Schedule

@dataclass
class Series:
    series_id: int
    name: str
    start_date: str
    end_date: str
    number_of_teams: int
    schedule: Schedule

    def get_series_winner(self) -> Optional[Team]:
        pass
