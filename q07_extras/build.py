# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    innings = [inning for _, inning in enumerate(data["innings"])]

    inning_overs = [inning[0] for inning in
                    [innings[x].values()[0].values() for x in range(2)]]
                    # range(2) coz only 2 inninngs per games

    innings_extras = []
    for deliveries in inning_overs:
        innings_extras.append(len(
            [v.values()[0]["runs"]["extras"] for i, v in enumerate(deliveries)
             if v.values()[0]["runs"]["extras"] > 0]
        ))

    difference = [abs(innings_extras[i + 1] - innings_extras[i])
                  for i in range(len(innings_extras) - 1)][0]

    return difference
