from dataclasses import dataclass
from typing import List
from datetime import date
from models.match import Match

@dataclass
class Schedule:
    tournament_name: str
    start_date: date
    end_date: date
    matches: List[Match]

    def get_schedule_info(self):
        info = []
        for m in self.matches:
            if isinstance(m.teams[0], dict):
                left_team = m.teams[0]["name"]
                right_team = m.teams[1]["name"]
            else:
                left_team = m.teams[0].name
                right_team = m.teams[1].name
            info.append(f"{m.date}: {left_team} vs {right_team} at {m.venue.name}")
        return info

    def get_matches_for_team(self, team_name: str):
        relevant = []
        for match in self.matches:
            if isinstance(match.teams[0], dict):
                if team_name in [match.teams[0]["name"], match.teams[1]["name"]]:
                    relevant.append(match)
            else:
                if team_name in [match.teams[0].name, match.teams[1].name]:
                    relevant.append(match)
        return relevant