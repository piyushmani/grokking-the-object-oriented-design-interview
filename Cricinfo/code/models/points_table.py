from dataclasses import dataclass
from typing import List
from .team import TeamStat

@dataclass
class PointsTable:
    points_table_id: int
    team_stats: List[TeamStat]

    def update_team_stats(self, team_stat: TeamStat):
        for i, stat in enumerate(self.team_stats):
            if stat.team.team_id == team_stat.team.team_id:
                self.team_stats[i] = team_stat
                break
        else:
            self.team_stats.append(team_stat)

    def get_rankings(self) -> List[TeamStat]:
        return sorted(
            self.team_stats,
            key=lambda x: (x.points, x.net_run_rate),
            reverse=True
        )
