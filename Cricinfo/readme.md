**Table of Contents**

- [System Requirements](#system-requirements)
- [Class diagram](#class-diagram)
- [Activity diagrams](#activity-diagrams)
- [Code](#code)

### System Requirements
- The system should be able to track the stats of all players, teams, and matches.
- The system should be able to track all scores or wickets that occurred for each ball. The system should also provide a live commentary for every ball.
- The system should be able to keep track of all matches—Test, T20, and ODI matches.
- The system should be able to keep track of ongoing and previous tournaments. The system should also be able to show a points table for all teams participating in a tournament.
- The system should be able to show the result of all previous televised matches.
- All teams should select some players who will participate in the tournament known as the tournament squad.
- For every match, the teams should be able to select 11 players to play on the field from the tournament squad, known as the playing eleven.
- The admin of the system should be able to add tournaments, matches, teams, players, and news to the system.

### Class diagram
------------

```mermaid
%%{init: { "theme": "neutral", "look": "handDrawn"} }%%
classDiagram
    class User {
        -username: String
        -email: String
        -password: String
        +login()
        +logout()
        +browseMatches()
        +sendNotification()
    }

    class Match {
        -matchId: String
        -teams: Team[2]
        -venue: Venue
        -series: Series
        -schedule: Schedule
        -innings: Innings[2]
        -umpires: Umpire[]
        -scorecard: Scorecard
        +getMatchDetails()
        +updateScore()
    }

    class Team {
        -teamId: String
        -name: String
        -players: Player[]
        +getTeamDetails()
    }

    class Player {
        -playerId: String
        -name: String
        -age: int
        -role: String
        +getPlayerStats()
    }

    class PlayerStats {
        -player: Player
        -matchesPlayed: int
        -runsScored: int
        -wicketsTaken: int
        +updateStats()
    }

    class Tournament {
        -tournamentId: String
        -name: String
        -format: String
        +getTournamentDetails()
        +getMatches()
    }

    class Commentary {
        -commentId: String
        -text: String
        -author: User
        -timestamp: Date
        +postComment()
    }

    class News {
        -newsId: String
        -headline: String
        -content: String
        -author: User
        -timestamp: Date
        +getNewsDetails()
    }

    class Innings {
        -inningsId: String
        -teamBatting: Team
        -score: int
        -wicketsLost: int
        -oversPlayed: float
        +updateScore()
    }

    class Over {
        -overNumber: int
        -bowler: Player
        -runsConceded: int
        -wicketsTaken: int
        +updateStats()
    }

    class Ball {
        -ballNumber: int
        -bowler: Player
        -batsman: Player
        -runsScored: int
        -wicket: Wicket
        -run: Run
        +recordBall()
    }

    class Run {
        -runType: String
    }

    class Wicket {
        -batsmanOut: Player
        -bowler: Player
        -dismissalType: String
        -fielder: Player
    }

    class Venue {
        -venueId: String
        -name: String
        -location: String
        -capacity: int
        +getVenueDetails()
    }

    class Series {
        -seriesId: String
        -name: String
        -format: String
        -matches: Match[]
        +getSeriesDetails()
    }

    class Schedule {
        -scheduleId: String
        -matches: Match[]
        +getScheduleDetails()
    }

    class Notification {
        -notificationId: String
        -type: String
        -content: String
        -recipient: User
        +sendNotification()
    }

    class Admin {
        -adminId: String
        -username: String
        -email: String
        -password: String
        +manageContent()
    }

    class Umpire {
        -umpireId: String
        -name: String
        -role: String
        +assignMatch()
    }

    class Scorecard {
        -match: Match
        -runsScoredTeam1: int
        -runsScoredTeam2: int
        -wicketsLostTeam1: int
        -wicketsLostTeam2: int
        -playerStats: PlayerStats[]
        +generateScorecard()
    }

    User --> Match
    Match "2" --> "1..2" Innings
    Innings --> Team
    Innings "1" --> "1" Match
    Innings "1" --> "1..*" Over
    Over "1" --> "1" Innings
    Over "1" --> "0..*" Ball
    Ball "1" --> "0..1" Run
    Ball "1" --> "0..1" Wicket
    Match "1" --> "1" Venue
    Match "0..1" --> "1..*" Series
    Series "0..*" --> "1" Match
    Schedule "1" --> "0..*" Match
    User "1" --> "0..*" Notification
    Admin --|> User
    Commentary --> User
    Commentary --> Match
    News --> User
    Player --> Team
    Player --> PlayerStats
    PlayerStats --> Player
    PlayerStats --> Tournament
    Tournament --> Match
    Match --> Umpire
    Match --> Scorecard
            
```

#### Activity Diagram (record of a ball)
------------
```mermaid

%%{init: { "theme": "forest", "look": "handDrawn",
"flowchart": {"nodeSpacing":10, "rankSpacing":20,"curve": "basic","useMaxWidth":true}} }%%

flowchart TD
 subgraph Ball["Ball"]
        B("Normal")
        C("Wide")
        D("No Ball")
        CA("Add 1 score to batting team")
        DA("Award next ball a free hit")
  end
 subgraph Out["Out"]
        J("Wicket")
        K("LBW")
        L("Caught out")
        M("Run out")
  end
    START["Start"] --> A("System adds  ball to the over")
    A --> A2("Select ball type")
    A2 --> Ball
    Ball --> F{{"Batter gets out ?"}}
    C --> CA
    D --> DA
    DA --> CA
    F -- No --> G("Record the score made")
    F -- Yes --> Out
    Out --> N("Ball commentary added")
    G --> N
    N --> P("Ball record saved")
    P --> END["END"]
     B:::normal
     C:::normal
     D:::normal
     CA:::normal
     DA:::normal
     J:::normal
     K:::normal
     L:::normal
     M:::normal
     START:::se
     A:::normal
     A2:::normal
     F:::question
     G:::normal
     N:::normal
     P:::normal
     END:::se
    classDef success fill:#FDFCFC, color:#73C6B6,stroke:#283747
    classDef error fill:#FDFCFC, color:#EC7063 ,stroke:#283747
    classDef question fill:#FDFCFC, color:#283747, stroke:#283747, stroke-width:1.5px, stroke-dasharray:3
    classDef normal fill:#FDFCFC, color:#283747, stroke:#6F6A68, stroke-width:1px
    classDef se fill:#FDFCFC, color:#283747, stroke:#6F6A68, stroke-width:2px
    style Ball stroke:#616161,fill:#FFFFFF
    style Out stroke:#616161,fill:#FFFFFF
    linkStyle 8 stroke:#D50000,fill:none
 
 ```
 
### Code
------------
> ***Note => In below code the database implementation are skiped.***

###### Enums and Constants
 
  ```python
  from abc import ABC
from enum import Enum

class MatchFormat(Enum):
    ODI = "One Day International"
    TEST = "Test Match"
    T20 = "Twenty20"

class PlayerRole(Enum):
    BATSMAN = "Batsman"
    BOWLER = "Bowler"
    ALL_ROUNDER = "All-Rounder"
    WICKET_KEEPER = "Wicket Keeper"

class DismissalType(Enum):
    BOWLED = "Bowled"
    CAUGHT = "Caught"
    RUN_OUT = "Run Out"
    LBW = "LBW"
    STUMPED = "Stumped"
    HIT_WICKET = "Hit Wicket"

class RunType(Enum):
    SINGLE = "Single"
    DOUBLE = "Double"
    TRIPLE = "Triple"
    FOUR = "Four"
    SIX = "Six"
    LEG_BYE = "Leg Bye"
    BYE = "Bye"
    NO_BALL = "No Ball"
    WIDE = "Wide"
```

#### User and Admin Class
```python

class User:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    def login(self):
        print(f"{self.username} logged in.")

    def logout(self):
        print(f"{self.username} logged out.")

    def browse_matches(self):
        pass

    def send_notification(self, message: str):
        print(f"Notification sent to {self.username}: {message}")


# Admin class inherits from User
class Admin(User):
    def manage_content(self):
        print(f"Admin {self.username} is managing content.")

```


#### Notification Class
```python
class Notification:
    def __init__(self, notification_id: str, notification_type: str, content: str, recipient: User):
        self.notification_id = notification_id
        self.type = notification_type
        self.content = content
        self.recipient = recipient

    def send_notification(self):
        self.recipient.send_notification(self.content)

```

#### Venue, Series and Schedule Class
```python

class Venue:
    def __init__(self, venue_id: str, name: str, location: str, capacity: int):
        self.venue_id = venue_id
        self.name = name
        self.location = location
        self.capacity = capacity

    def get_venue_details(self):
        return {"name": self.name, "location": self.location, "capacity": self.capacity}


class Series:
    def __init__(self, series_id: str, name: str, match_format: MatchFormat):
        self.series_id = series_id
        self.name = name
        self.format = match_format
        self.matches: List['Match'] = []

    def get_series_details(self):
        return {"name": self.name, "format": self.format.name}


class Schedule:
    def __init__(self, schedule_id: str):
        self.schedule_id = schedule_id
        self.matches: List['Match'] = []

    def get_schedule_details(self):
        return {"schedule_id": self.schedule_id, "matches": len(self.matches)}

```


#### Player, PlayerStats, Team, and TeamStat Class
```python

class Player:
    def __init__(self, player_id: str, name: str, age: int, role: PlayerRole):
        self.player_id = player_id
        self.name = name
        self.age = age
        self.role = role
        self.stats = PlayerStats(self, 0, 0, 0)

    def get_player_stats(self):
        return {"matches_played": self.stats.matches_played, "runs_scored": self.stats.runs_scored, "wickets_taken": self.stats.wickets_taken}

class PlayerStats:
    def __init__(self, player: 'Player', matches_played: int, runs_scored: int, wickets_taken: int):
        self.player = player
        self.matches_played = matches_played
        self.runs_scored = runs_scored
        self.wickets_taken = wickets_taken

    def update_stats(self, runs: int, wickets: int):
        self.runs_scored += runs
        self.wickets_taken += wickets

class Team:
    def __init__(self, team_id: str, name: str):
        self.team_id = team_id
        self.name = name
        self.players: List[Player] = []

    def get_team_details(self):
        return {"team_id": self.team_id, "name": self.name, "players": [player.name for player in self.players]}

class TeamStat:
    def __init__(self, team: Team):
        self.team = team
        self.matches_played = 0
        self.wins = 0
        self.losses = 0

    def get_team_stats(self):
        return {"team": self.team.name, "matches_played": self.matches_played, "wins": self.wins, "losses": self.losses}

```


#### Over, Ball, Wicket, and, Run Class
```python

class Over:
    def __init__(self, over_number: int, bowler: Player):
        self.over_number = over_number
        self.bowler = bowler
        self.balls: List[Ball] = []

    def update_stats(self):
        return sum(ball.run.runs for ball in self.balls), len([ball for ball in self.balls if ball.wicket])

class Ball:
    def __init__(self, ball_number: int, bowler: Player, batsman: Player, run: Run, wicket: Optional[Wicket] = None):
        self.ball_number = ball_number
        self.bowler = bowler
        self.batsman = batsman
        self.run = run
        self.wicket = wicket

    def record_ball(self):
        return {"ball_number": self.ball_number, "runs": self.run.runs, "wicket": self.wicket is not None}

class Wicket:
    def __init__(self, batsman_out: Player, bowler: Player, dismissal_type: DismissalType, fielder: Optional[Player]):
        self.batsman_out = batsman_out
        self.bowler = bowler
        self.dismissal_type = dismissal_type
        self.fielder = fielder


class Run:
    def __init__(self, run_type: RunType, runs: int):
        self.run_type = run_type
        self.runs = runs



```


#### Abstract classes for Odi, Test, and T20
``` python
from abc import ABC, abstractmethod

class MatchFormatBase(ABC):
    @abstractmethod
    def get_format_name(self):
        pass


class Odi(MatchFormatBase):
    def get_format_name(self):
        return "One Day International"


class Test(MatchFormatBase):
    def get_format_name(self):
        return "Test Match"


class T20(MatchFormatBase):
    def get_format_name(self):
        return "Twenty20"

 ```

#### Match, Playing11, Innings, Scoreboard

```python

class Match:
    def __init__(self, match_id: str, teams: List[Team], venue: Venue, series: Series, schedule: Schedule):
        self.match_id = match_id
        self.teams = teams
        self.venue = venue
        self.series = series
        self.schedule = schedule
        self.innings: List[Innings] = []
        self.umpires: List['Umpire'] = []
        self.scorecard = Scorecard(self)

    def get_match_details(self):
        return {
            "match_id": self.match_id,
            "venue": self.venue.get_venue_details(),
            "series": self.series.get_series_details(),
            "teams": [team.get_team_details() for team in self.teams]
        }

    def update_score(self):
        for inning in self.innings:
            inning.update_score()

class Playing11:
    def __init__(self, team: Team):
        self.team = team
        self.players: List[Player] = []

    def get_playing11(self):
        return [player.name for player in self.players]

class Innings:
    def __init__(self, innings_id: str, team_batting: Team):
        self.innings_id = innings_id
        self.team_batting = team_batting
        self.score = 0
        self.wickets_lost = 0
        self.overs_played = 0.0
        self.overs: List[Over] = []

    def update_score(self):
        for over in self.overs:
            runs, wickets = over.update_stats()
            self.score += runs
            self.wickets_lost += wickets


class Scorecard:
    def __init__(self, match: 'Match'):
        self.match = match
        self.runs_scored_team1 = 0
        self.runs_scored_team2 = 0
        self.wickets_lost_team1 = 0
        self.wickets_lost_team2 = 0

    def generate_scorecard(self):
        return {
            "team1": {"runs": self.runs_scored_team1, "wickets": self.wickets_lost_team1},
            "team2": {"runs": self.runs_scored_team2, "wickets": self.wickets_lost_team2}
        }

```

#### Tournament, PointsTable 

```python
class Tournament:
    def __init__(self, tournament_id: str, name: str, format: MatchFormat):
        self.tournament_id = tournament_id
        self.name = name
        self.format = format
        self.matches: List[Match] = []

    def get_tournament_details(self):
        return {"name": self.name, "format": self.format.name}

    def get_matches(self):
        return [match.get_match_details() for match in self.matches]

class PointsTable:
    def __init__(self):
        self.teams: List[Team] = []
        self.points: dict = {}

    def update_points(self, team: Team, points: int):
        self.points[team.team_id] = points

```

#### Commentator and Commentary

```python
class Commentator:
    def __init__(self, commentator_id: str, name: str):
        self.commentator_id = commentator_id
        self.name = name

    def provide_commentary(self, text: str):
        print(f"{self.name}: {text}")

class Commentary:
    def __init__(self, comment_id: str, text: str, author: User, timestamp: datetime):
        self.comment_id = comment_id
        self.text = text
        self.author = author
        self.timestamp = timestamp

    def post_comment(self):
        return f"{self.author.username}: {self.text} (Posted at {self.timestamp})"

```
#### News class
```python
class News:
    def __init__(self, news_id: str, headline: str, content: str, author: User, timestamp: datetime):
        self.news_id = news_id
        self.headline = headline
        self.content = content
        self.author = author
        self.timestamp = timestamp

    def get_news_details(self):
        return {"headline": self.headline, "content": self.content, "author": self.author.username, "timestamp": self.timestamp}
```

#### Umpire class

```python
class Umpire:
    def __init__(self, umpire_id: str, name: str, role: str):
        self.umpire_id = umpire_id
        self.name = name
        self.role = role

    def assign_match(self, match: Match):
        match.umpires.append(self)

```