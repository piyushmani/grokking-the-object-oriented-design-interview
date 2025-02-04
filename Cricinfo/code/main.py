
from datetime import date
import random
from models.player import Player
from models.innings import Innings
from models.series import Series
from models.schedule import Schedule
from models.over import Over
from models.wicket import Wicket
from models.run import Run
from models.ball import Ball
from models.match import OdiMatch
from data_generator import determine_batting_order, generate_team_object, generate_venues, get_toss_decision
from models.tournament import Tournament
from models.points_table import PointsTable

def simulate_match():
    # Generate some sample venues
    match_venues = generate_venues()

    # 2) Setup a sample tournament 
    world_cup_2011 = Tournament(
        name="ICC Cricket World Cup",
        year=2011,
        start_date="2011-02-19",
        end_date="2011-04-02",
        host_country="India",
        teams=[],
        venues=match_venues,
        series=[],
        points_table=PointsTable(points_table_id=1, team_stats=[]),
        winner=None
    )

    # Generate two teams as Team objects
    team_names = ["India", "New Zealand"]
    team1 = generate_team_object(1, team_names[0])
    team2 = generate_team_object(2, team_names[1])
    all_teams = [team1, team2]
    
    # Create an ODI match from these two teams
    match = OdiMatch(
        match_id=1,
        teams=all_teams,  # list of two Team objects
        venue=match_venues[0],
        date="2011-02-19",
        start_time="14:30",
        toss_winner=None,
        toss_decision=None
    )
    
    print(f"--- MatchID={match.match_id}: {team1.name} vs {team2.name} ---")
    
    #  Decide toss
    toss_winner = random.choice(all_teams)
    toss_decision = get_toss_decision()
    match.set_toss_winner(toss_winner)
    match.set_toss_decision(toss_decision)

    # Determine who bats first and second
    batting_first, bowling_first = determine_batting_order(toss_winner, toss_decision, team1, team2)
    # For clarity, the team batting second is:
    batting_second = team1 if batting_first != team1 else team2

    print(f"{toss_winner.name} won the toss and chose to {toss_decision}.")
    print(f"Batting First: {batting_first.name}, Bowling First: {bowling_first.name}")
    print("------------------------------------------------------")

    # First Innings Simulation
    first_innings = Innings(
        innings_id=1,
        batting_team=batting_first,
        bowling_team=bowling_first
    )
    
    # Prepare batting order for the first innings (assume 12 players)
    batting_order_1 = [Player(player_id=100 + i, name=f"Batsman_{i}", role="Batsman", batting_style="Right-handed", bowling_style="None") for i in range(1, 13)]
    # Two batsmen start at the crease
    current_batsmen_1 = [batting_order_1.pop(0), batting_order_1.pop(0)]
    
    overs_to_simulate = 5  # Change this to simulate a full innings

    for over_num in range(1, overs_to_simulate + 1):
        bowler = Player(
            player_id=800 + over_num,
            name=f"Bowler_{over_num}",
            role="Bowler",
            batting_style="Right-handed",
            bowling_style="Right-arm Fast"
        )
        over_obj = Over(over_number=over_num, bowler=bowler)
        runs_this_over = 0
        wickets_this_over = 0
        
        for ball_num in range(1, 7):
            current_striker = current_batsmen_1[0]
            runs_scored = random.choice([0, 1, 2, 3, 4, 6])
            wicket_chance = (random.random() < 0.15)
            wicket_obj = None

            if wicket_chance:
                wicket_obj = Wicket(
                    batsman=current_striker,
                    bowler=bowler,
                    wicket_type=random.choice(["caught", "bowled", "lbw", "run out"])
                )
                wickets_this_over += 1

            run_obj = Run(runs=runs_scored)
            commentary_str = (
                f"Over {over_num}.{ball_num} - {current_striker.name} vs {bowler.name} | "
                f"Runs: {runs_scored}" + (" | WICKET!" if wicket_chance else "")
            )
            ball = Ball(
                ball_number=ball_num,
                run=run_obj,
                wicket=wicket_obj,
                batsman=current_striker,
                bowler=bowler,
                commentary=commentary_str
            )
            over_obj.add_ball(ball)
            runs_this_over += runs_scored

            print(ball.commentary)
            
            if wicket_chance:
                if batting_order_1:
                    new_batsman = batting_order_1.pop(0)
                    current_batsmen_1[0] = new_batsman
            else:
                if runs_scored % 2 == 1:
                    current_batsmen_1[0], current_batsmen_1[1] = current_batsmen_1[1], current_batsmen_1[0]
                    
        first_innings.add_over(over_obj)
        print(f"** Over {over_num} Summary => Runs: {runs_this_over}, Wickets: {wickets_this_over} **")
        print(f"Current Score: {first_innings.total_runs}/{first_innings.wickets}")
        print("------------------------------------------------------")
    
    print(
        f"End of Innings 1 => {batting_first.name}: "
        f"{first_innings.total_runs}/{first_innings.wickets} in {overs_to_simulate} overs."
    )
    first_innings_score = first_innings.total_runs
    print("\n--- First Innings Complete ---\n")
    
    # Second Innings Simulation (Team batting second chases the target)
    second_innings = Innings(
        innings_id=2,
        batting_team=batting_second,
        bowling_team=batting_first  # Bowling team is the team that batted first
    )
    
    # Prepare batting order for the second innings (assume 12 players)
    batting_order_2 = [Player(player_id=200 + i, name=f"Batsman_{i}_2", role="Batsman", batting_style="Right-handed", bowling_style="None") for i in range(1, 13)]
    current_batsmen_2 = [batting_order_2.pop(0), batting_order_2.pop(0)]
    
    print(f"{batting_second.name} needs to chase a target of {first_innings_score + 1} runs!")
    print("------------------------------------------------------")
    
    # We'll simulate overs until either overs are exhausted or target is reached.
    target = first_innings_score + 1
    over_num = 1
    while over_num <= overs_to_simulate and second_innings.total_runs < target:
        bowler = Player(
            player_id=900 + over_num,
            name=f"Bowler2_{over_num}",
            role="Bowler",
            batting_style="Right-handed",
            bowling_style="Right-arm Fast"
        )
        over_obj = Over(over_number=over_num, bowler=bowler)
        runs_this_over = 0
        wickets_this_over = 0
        
        for ball_num in range(1, 7):
            current_striker = current_batsmen_2[0]
            runs_scored = random.choice([0, 1, 2, 3, 4, 6])
            wicket_chance = (random.random() < 0.15)
            wicket_obj = None

            if wicket_chance:
                wicket_obj = Wicket(
                    batsman=current_striker,
                    bowler=bowler,
                    wicket_type=random.choice(["caught", "bowled", "lbw", "run out"])
                )
                wickets_this_over += 1

            run_obj = Run(runs=runs_scored)
            commentary_str = (
                f"Over {over_num}.{ball_num} - {current_striker.name} vs {bowler.name} | "
                f"Runs: {runs_scored}" + (" | WICKET!" if wicket_chance else "")
            )
            ball = Ball(
                ball_number=ball_num,
                run=run_obj,
                wicket=wicket_obj,
                batsman=current_striker,
                bowler=bowler,
                commentary=commentary_str
            )
            over_obj.add_ball(ball)
            runs_this_over += runs_scored

            print(ball.commentary)
            
            if wicket_chance:
                if batting_order_2:
                    new_batsman = batting_order_2.pop(0)
                    current_batsmen_2[0] = new_batsman
            else:
                if runs_scored % 2 == 1:
                    current_batsmen_2[0], current_batsmen_2[1] = current_batsmen_2[1], current_batsmen_2[0]
            
            # If target reached mid-over, break out
            if second_innings.total_runs + runs_this_over >= target:
                break
                
        second_innings.add_over(over_obj)
        print(f"** Over {over_num} Summary => Runs: {runs_this_over}, Wickets: {wickets_this_over} **")
        print(f"Current Score: {second_innings.total_runs}/{second_innings.wickets}")
        print("------------------------------------------------------")
        over_num += 1
        
    print(
        f"End of Innings 2 => {batting_second.name}: "
        f"{second_innings.total_runs}/{second_innings.wickets} in {over_num - 1} overs."
    )
    
    # 9) Declare Winner
    if second_innings.total_runs >= target:
        print(f"\n{batting_second.name} wins by {10 - second_innings.wickets} wickets!")
    elif second_innings.total_runs < target:
        print(f"\n{batting_first.name} wins by {target - second_innings.total_runs - 1} runs!")
    else:
        print("\nThe match is a Tie!")
        
    print("\n--- Simulation Complete ---")

if __name__ == "__main__":
    simulate_match()
        