# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    # Write your code here
    overs = data["innings"][1]["2nd innings"]["deliveries"]
    for balls in overs:
        for ball in balls:
            for out in balls[ball]:
                if out == "wicket":
                    if balls[ball][out]["kind"] == "bowled":
                        bowled_players.append(balls[ball][out]["player_out"])

    return bowled_players
