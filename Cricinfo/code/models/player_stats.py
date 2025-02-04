from dataclasses import dataclass

@dataclass
class PlayerStats:
    player_id: int
    matches: int
    runs: int
    wickets: int
    average: float

    def get_summary(self) -> str:
        return (
            f"Player {self.player_id} - Matches: {self.matches}, "
            f"Runs: {self.runs}, Wickets: {self.wickets}, "
            f"Average: {self.average:.2f}"
        )