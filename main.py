
import random

class Player:
    def __init__(self, name, bowling, batting, fielding, running, experience):
        self.name = name
        self.bowling = bowling
        self.batting = batting
        self.fielding = fielding
        self.running = running
        self.experience = experience

class Teams:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batting_order = []

    def select_captain(self):
        self.captain = random.choice(self.players)

    def send_next_player(self):
        if self.batting_order:
            return self.batting_order.pop(0)
        else:
            return None

    def choose_bowler(self):
        return random.choice(self.players)

    def decide_batting_order(self):
        self.batting_order = random.sample(self.players, len(self.players))

class Field:
    def __init__(self, field_size, fan_ratio, pitch_conditions, home_advantage):
        self.field_size = field_size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage

class Umpire:
    def __init__(self):
        self.scores = 0
        self.wickets = 0
        self.overs = 0

    def predict_outcome(self, batsman, bowler):
        batting_probability = batsman.batting * random.random()
        bowling_probability = bowler.bowling * random.random()

        if batting_probability > bowling_probability:
            return "Out"
        else:
            return "Safe"

    def update_score(self, runs):
        self.scores += runs

    def update_wickets(self):
        self.wickets += 1

    def update_overs(self):
        self.overs += 1

class Commentator:
    def __init__(self, match):
        self.match = match

    def comment_ball(self, batsman, bowler, outcome, runs):
        if outcome == "Out":
            print(f"{batsman.name} is out bowled by {bowler.name}.\n")
        else:
            print(f"{batsman.name} plays it safely against {bowler.name}. {runs} runs scored.\n")

    def comment_over(self):
        print(f"End of over {self.match.umpire.overs}.")

class Match:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = Umpire()
        self.commentator = Commentator(self)

    def start_match(self):
        self.team1.select_captain()
        self.team2.select_captain()
        self.team1.decide_batting_order()
        self.team2.decide_batting_order()

        self.play_innings(self.team1, self.team2)
        self.play_innings(self.team2, self.team1)

    def play_innings(self, batting_team, bowling_team):
        for _ in range(50):
            batsman = batting_team.send_next_player()
            if batsman is None:
                break

            bowler = bowling_team.choose_bowler()

            outcome = self.umpire.predict_outcome(batsman, bowler)

            if outcome == "Out":
                self.umpire.update_wickets()
            else:
                runs = self.calculate_runs(batsman, bowler)
                self.umpire.update_score(runs)

            self.commentator.comment_ball(batsman, bowler, outcome, runs if outcome != "Out" else 0)

            self.umpire.update_overs()

            if self.umpire.wickets == 10:
                break

            if self.umpire.overs % 6== 0:
                self.commentator.comment_over()

    def calculate_runs(self, batsman, bowler):
        # print("Runs")
        return int((batsman.batting + bowler.bowling) * random.random() * 6)

    def end_match(self):
        print("Match Ended.")
        print(f"Total Score: {self.umpire.scores}/{self.umpire.wickets} \n")


# Example usage
 

print(" ")
print("India vs South Africa !!!! \n")
player1 = Player("MS Dhoni", 0.2, 0.8, 0.99, 0.8, 0.9)
player2 = Player("Virat Kohli", 0.1, 0.9, 0.95, 0.7, 0.8)
player3 = Player("Rohit Sharma", 0.1, 0.85, 0.9, 0.75, 0.7)
# Player4 = Player("Sachin Tendulkar",0.3,0.80,0.98,0.8)
players_team1 = [player1, player2, player3]

player4 = Player("Lungi Ngidi", 0.2, 0.8, 0.99, 0.8, 0.9)
player5 = Player("Chris Morris", 0.1, 0.9, 0.95, 0.7, 0.8)
player6 = Player("Imran Tahir", 0.1, 0.85, 0.9, 0.75, 0.7)
players_team2 = [player4, player5, player6]

team1 = Teams("Team 1", players_team1)
team2 = Teams("Team 2", players_team2)

field = Field("Medium", 0.7, "Dry", 0.1)

match = Match(team1, team2, field)
match.start_match()
print("Calculated Runs:",match.calculate_runs(player1,player5))
match.end_match()

