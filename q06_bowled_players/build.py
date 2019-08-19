# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here

    bowled_players = []

    firstinnings = data["innings"][0]["1st innings"]["deliveries"]
    secondinnings = data["innings"][1]["2nd innings"]["deliveries"]

    for bowler in firstinnings:
        for delivery, info in bowler.items():
            if info.has_key('wicket'):
                if info["wicket"]["kind"] == 'bowled':
                    bowled_players.append(info["wicket"]["player_out"])

    for bowler in secondinnings:
        for delivery, info in bowler.items():
            if info.has_key('wicket'):
                if info["wicket"]["kind"] == 'bowled':
                    bowled_players.append(info["wicket"]["player_out"])

    return bowled_players
