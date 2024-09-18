from datetime import datetime
import random
from enum import Enum

# Enum for match formats
class MatchFormat(Enum):
    ODI = "ODI"
    TEST = "Test"
    T20 = "T20"

class RunType(Enum):
    NORMAL = "Normal"
    FOUR = "Four"
    SIX = "Six"

class NotificationType(Enum):
    MATCH_START = "Match Start"
    MATCH_END = "Match End"

# Classes for Users, Admins, and Commentators
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def login(self):
        return f"{self.username} logged in."

    def send_notification(self, notification):
        print(f"Notification to {self.username}: {notification.content}")

class Admin(User):
    def manage_content(self):
        return f"Admin {self.username} is managing content."

class Commentator(User):
    def commentate(self, text):
        return f"Commentator {self.username} says: {text}"

class Notification:
    def __init__(self, notification_id, notification_type, content, recipient):
        self.notification_id = notification_id
        self.notification_type = notification_type
        self.content = content
        self.recipient = recipient

    def send(self):
        self.recipient.send_notification(self)

# Class for Venue
class Venue:
    def __init__(self, venue_id, name, location, capacity):
        self.venue_id = venue_id
        self.name = name
        self.location = location
        self.capacity = capacity

# Class for Series and Tournament
class Series:
    def __init__(self, series_id, name, format):
        self.series_id = series_id
        self.name = name
        self.format = format
        self.matches = []

class Tournament:
    def __init__(self, tournament_id, name, format):
        self.tournament_id = tournament_id
        self.name = name
        self.format = format
        self.series = []

# Classes for Teams and Players
class Player:
    def __init__(self, player_id, name, age, role):
        self.player_id = player_id
        self.name = name
        self.age = age
        self.role = role
        self.stats = PlayerStats(self)

class PlayerStats:
    def __init__(self, player):
        self.player = player
        self.matches_played = 0
        self.runs_scored = 0
        self.wickets_taken = 0

    def update_stats(self, runs, wickets):
        self.runs_scored += runs
        self.wickets_taken += wickets

class Team:
    def __init__(self, team_id, name):
        self.team_id = team_id
        self.name = name
        self.players = []
        self.playing11 = Playing11()

    def add_player(self, player):
        self.players.append(player)

class Playing11:
    def __init__(self):
        self.players = []

    def set_playing11(self, players):
        self.players = players[:11]

class TeamStat:
    def __init__(self, team):
        self.team = team
        self.wins = 0
        self.losses = 0

class PointsTable:
    def __init__(self):
        self.teams = {}

    def update_points(self, team, points):
        if team not in self.teams:
            self.teams[team] = 0
        self.teams[team] += points

# Classes for Match, Innings, Over, Ball, Run, Wicket
class Innings:
    def __init__(self, innings_id, team_batting):
        self.innings_id = innings_id
        self.team_batting = team_batting
        self.score = 0
        self.wickets_lost = 0
        self.overs_played = 0

class Over:
    def __init__(self, over_number, bowler):
        self.over_number = over_number
        self.bowler = bowler
        self.balls = []

    def add_ball(self, ball):
        self.balls.append(ball)

class Ball:
    def __init__(self, ball_number, bowler, batsman, run, wicket=None):
        self.ball_number = ball_number
        self.bowler = bowler
        self.batsman = batsman
        self.run = run
        self.wicket = wicket

    def record_ball(self):
        if self.wicket:
            return f"WICKET! {self.wicket.batsman_out.name} was out."
        else:
            return f"Ball {self.ball_number}: {self.batsman.name} scored {self.run.runs} runs."

class Run:
    def __init__(self, run_type, runs):
        self.run_type = run_type
        self.runs = runs

class Wicket:
    def __init__(self, batsman_out, bowler, dismissal_type):
        self.batsman_out = batsman_out
        self.bowler = bowler
        self.dismissal_type = dismissal_type

class Match:
    def __init__(self, match_id, teams, venue, series):
        self.match_id = match_id
        self.teams = teams
        self.venue = venue
        self.series = series
        self.scorecard = Scorecard(self)

    def start_match(self):
        print(f"Match {self.match_id} started between {self.teams[0].name} and {self.teams[1].name} at {self.venue.name}.")
        self.scorecard.generate_scorecard()

class Scorecard:
    def __init__(self, match):
        self.match = match

    def generate_scorecard(self):
        print(f"Generating scorecard for match {self.match.match_id}...")

# Commentary and News Classes
class Commentary:
    def __init__(self, comment_id, text, author, timestamp):
        self.comment_id = comment_id
        self.text = text
        self.author = author
        self.timestamp = timestamp

    def post_comment(self):
        print(f"{self.author.username} commented: {self.text}")

class News:
    def __init__(self, news_id, headline, content, author, timestamp):
        self.news_id = news_id
        self.headline = headline
        self.content = content
        self.author = author
        self.timestamp = timestamp

    def get_news_details(self):
        print(f"News: {self.headline} - {self.content} by {self.author.username}")

# Odi, Test, and T20 are abstract match formats
class Odi(Match):
    def __init__(self, match_id, teams, venue, series):
        super().__init__(match_id, teams, venue, series)

class Test(Match):
    def __init__(self, match_id, teams, venue, series):
        super().__init__(match_id, teams, venue, series)

# Schedule Class
class Schedule:
    def __init__(self, schedule_id, matches):
        self.schedule_id = schedule_id
        self.matches = matches

    def get_schedule_details(self):
        print(f"Schedule {self.schedule_id} contains {len(self.matches)} matches.")


# Match Simulation
def simulate_match():
    # Create Users
    user1 = User("user001", "user1@example.com", "pass123")
    admin = Admin("admin001", "admin@example.com", "adminpass")
    commentator = Commentator("commentator001", "commentator@example.com", "pass456")

    # Create Teams and Players
    team1 = Team("team001", "Team A")
    team2 = Team("team002", "Team B")

    for i in range(11):
        team1.add_player(Player(f"playerA{i+1}", f"Player A{i+1}", 25 + i, "Batsman"))
        team2.add_player(Player(f"playerB{i+1}", f"Player B{i+1}", 25 + i, "Bowler"))

    team1.playing11.set_playing11(team1.players)
    team2.playing11.set_playing11(team2.players)

    # Create Venue, Series, and Match
    venue = Venue("venue001", "Stadium A", "City X", 50000)
    series = Series("series001", "Series 1", MatchFormat.T20)
    match = T20("match001", [team1, team2], venue, series)  # Using T20 format

    # Start Match
    match.start_match()

    # Create Commentary and News
    commentary1 = Commentary("c001", "Match has started!", commentator, datetime.now())
    commentary1.post_comment()

    news1 = News("news001", "Match update", "Team A is off to a great start!", commentator, datetime.now())
    news1.get_news_details()

    # Create a schedule
    schedule = Schedule("schedule001", [match])
    schedule.get_schedule_details()

    # Simulate an Over
    bowler = team2.players[0]
    over = Over(1, bowler)

    for ball_number in range(6):
        batsman = team1.players[random.randint(0, 10)]
        run_scored = random.randint(0, 6)
        run_type = RunType.SIX if run_scored == 6 else RunType.NORMAL
        ball = Ball(ball_number, bowler, batsman, Run(run_type, run_scored))
        print(ball.record_ball())

    # Post Match End Notification
    notification = Notification("notif001", NotificationType.MATCH_END, "Match has ended.", user1)
    notification.send()


simulate_match()
