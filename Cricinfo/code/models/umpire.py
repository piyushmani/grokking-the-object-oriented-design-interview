from dataclasses import dataclass

@dataclass
class Umpire:
    umpire_id: int
    name: str
    country: str
    matches_officiated: int

    def increment_matches_officiated(self):
        self.matches_officiated += 1