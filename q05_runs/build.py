# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

deliveries=data["innings"][0]["1st innings"]["deliveries"]

def BC_runs(data):
    runs=0
    for balls in deliveries:
        for key, value in balls.items():
            if balls[key]["batsman"] == 'BB McCullum':
                runs += balls[key]["runs"]["batsman"]
    return(runs)
