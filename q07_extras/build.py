# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
addn_run=[0, 0]

def extras_runs(data=data):
    difference = 0

    for inning in range(0,2):
        deliveries = data["innings"][inning]

        for key, value in deliveries.items():
            overs = deliveries[key]["deliveries"]

            for balls in overs:

                for key, value in balls.items():

                    if balls[key]["runs"]["extras"] > 0 and "byes" not in balls[key]["extras"].keys():
                        addn_run[inning] += balls[key]["runs"]["extras"]

    difference = addn_run[inning]-addn_run[inning-1]

    return difference
