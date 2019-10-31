# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

bowled_players = []
def bowled_out(data=data):
    for inning in range(0,2):
        deliveries = data["innings"][inning]
        for key, value in deliveries.items():
            overs = deliveries[key]["deliveries"]
            for balls in overs:
                for key, value in balls.items():
                    if (balls[key].get("wicket","NA") != "NA" and balls[key]["wicket"]["kind"] == "bowled"):
                        bowled_players.append(balls[key]["batsman"])

    return bowled_players
