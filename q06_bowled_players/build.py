# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    innings = [inning for _, inning in enumerate(data["innings"])]

    deliveries = [overs for inning in
                  [innings[x].values()[0].values() for x in range(2)]
                  # range(2) coz only 2 innings per game
                  for overs in inning[0]]

    bowled_players = []
    for _, v in enumerate(deliveries):
        if "wicket" in v.values()[0]:
            if v.values()[0]["wicket"]["kind"] == "bowled":
                bowled_players.append(v.values()[0]["wicket"]["player_out"])

    return bowled_players
