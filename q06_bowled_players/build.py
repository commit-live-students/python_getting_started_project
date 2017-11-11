# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
global bowled_players
# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players=[]
    deliveries_data=data["innings"][1]["2nd innings"]["deliveries"]
    for i in range(0, len(deliveries_data)):
            keys=deliveries_data[i].keys()
            if ('wicket' in deliveries_data[i][keys[0]]) and ((deliveries_data[i][keys[0]]["wicket"]["kind"]) == "bowled"):
                bowled_players.append(deliveries_data[i][keys[0]]["wicket"]["player_out"])

    return bowled_players
