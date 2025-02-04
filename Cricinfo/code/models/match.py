from dataclasses import dataclass
from typing import List, Optional
from enum import Enum
from abc import ABC, abstractmethod
from .team import Team
from .venue import Venue

class Match(ABC):
    """Abstract base for ODI, Test, T20 matches."""
    def __init__(
        self,
        match_id: int,
        teams: List,
        venue: Venue,
        date: str,
        start_time: str,
        toss_winner=None,
        toss_decision: Optional[str] = None,
        result: Optional[str] = None,
        man_of_the_match: Optional[str] = None
    ):
        self.match_id = match_id
        self.teams = teams
        self.venue = venue
        self.date = date
        self.start_time = start_time
        self.toss_winner = toss_winner
        self.toss_decision = toss_decision
        self.result = result
        self.man_of_the_match = man_of_the_match

    @abstractmethod
    def get_match_type(self) -> str:
        pass

    def update_result(self, result: str):
        self.result = result

    def set_man_of_the_match(self, player: str):
        self.man_of_the_match = player

    def set_toss_winner(self, team):
        self.toss_winner = team

    def set_toss_decision(self, toss_decision):
        self.toss_decision = toss_decision

class OdiMatch(Match):
    def get_match_type(self) -> str:
        return "ODI"

class TestMatch(Match):
    def get_match_type(self) -> str:
        return "Test"

class T20Match(Match):
    def get_match_type(self) -> str:
        return "T20"