from ..services.match_factory import MatchFactory
from ..enums.match_type import MatchType
from ..models.team import Team
from ..models.venue import Venue

class MatchController:
    def setup_match(self, match_type: MatchType):
        team1 = Team(team_id=1, name="Team A", short_name="A", flag_url="http://flagA.com")
        team2 = Team(team_id=2, name="Team B", short_name="B", flag_url="http://flagB.com")

        venue = Venue(
            venue_id=1,
            name="Stadium A",
            city="City A",
            country="Country A",
            capacity=50000,
            hosted_matches=10
        )

        match = MatchFactory.create_match(
            match_type,
            match_id="m001",
            teams=[team1, team2],
            venue=venue,
            date="2025-01-01",
            start_time="10:00",
            toss_winner=None,
            toss_decision="Bat"
        )
        return match

    def start_match(self, match):
        print("Match is starting...")
        print(
            f"Match ID: {match.match_id} between "
            f"{match.teams[0].name} and {match.teams[1].name}"
        )
        print(f"Venue: {match.venue.name}, Date: {match.date}")
