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
%%{init: { "theme": "neutral"} }%%
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

