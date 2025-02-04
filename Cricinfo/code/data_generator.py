from random import randint
from faker import Faker

from models.team import Team
from models.umpire import Umpire
from models.venue import Venue
from models.player import Player

faker = Faker()

def generate_venues():
    wankhede_stadium = Venue(
        venue_id=1,
        name="Wankhede Stadium",
        city="Mumbai",
        country="India",
        capacity=33000,
        hosted_matches=6
    )
    eden_gardens = Venue(
        venue_id=2,
        name="Eden Gardens",
        city="Kolkata",
        country="India",
        capacity=68000,
        hosted_matches=5
    )
    premadasa_stadium = Venue(
        venue_id=3,
        name="R. Premadasa Stadium",
        city="Colombo",
        country="Sri Lanka",
        capacity=35000,
        hosted_matches=8
    )
    sher_e_bangla_stadium = Venue(
        venue_id=4,
        name="Sher-e-Bangla National Stadium",
        city="Dhaka",
        country="Bangladesh",
        capacity=25000,
        hosted_matches=9
    )
    return [
        wankhede_stadium,
        eden_gardens,
        premadasa_stadium,
        sher_e_bangla_stadium
    ]


def generate_player(player_id: int):
    return {
        "player_id": player_id,
        "name": faker.name(),
        "role": faker.random_element(elements=["Batsman", "Bowler", "All-Rounder", "Wicketkeeper"]),
        "batting_style": faker.random_element(elements=["Right-handed", "Left-handed"]),
        "bowling_style": faker.random_element(elements=["Right-arm Fast", "Left-arm Spin", "None"]),
    }

def generate_team_object(team_id: int, team_name: str, num_players: int = 15):
    players = [Player(**generate_player(i)) for i in range(1, num_players+1)]
    return Team(
        team_id=team_id,
        name=team_name,
        short_name=faker.country_code(),
        flag_url=faker.image_url(),
        players=players
    )

def generate_umpires():
    return [
        Umpire(
            umpire_id=1,
            name=faker.name(),
            country="India",
            matches_officiated=randint(20, 100)
        ),
        Umpire(
            umpire_id=2,
            name=faker.name(),
            country="Australia",
            matches_officiated=randint(20, 100)
        ),
    ]


def get_toss_decision():
    """Randomly decide 'Bat' or 'Bowl'."""
    return faker.random_element(elements=["Bat", "Bowl"])  

def determine_batting_order(toss_winner, toss_decision, team1, team2):
    if toss_decision == "Bat":
        batting_first = toss_winner
        batting_second = team2 if toss_winner == team1 else team1
    else:
        batting_first = team2 if toss_winner == team1 else team1
        batting_second = toss_winner
    return batting_first, batting_second

def is_wicket_ball():
    """5% chance of a wicket."""
    wicket_chance = randint(0, 100)
    return wicket_chance < 5
       