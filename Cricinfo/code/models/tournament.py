from dataclasses import dataclass
from typing import List, Optional
from models.series import Series
from models.team import Team
from models.schedule import Schedule
from models.points_table import PointsTable
from models.venue import Venue

@dataclass
class Tournament:
    name: str
    year: int
    start_date: str
    end_date: str
    host_country: str
    teams: List[Team]
    venues: List[Venue]
    series: List[Series]
    points_table: PointsTable
    winner: Optional[Team]

    def get_tournament_info(self):
        return f"{self.name} {self.year} hosted in {self.host_country}."

    def get_winner(self):
        if self.winner:
            return f"The winner of {self.name} {self.year} is {self.winner.name}."
        return "No winner decided yet."