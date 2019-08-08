# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs = 0
    # Write your code here
    overs = data["innings"][0]["1st innings"]["deliveries"]
    for balls in overs:
        for ball in balls:
            if balls[ball]["batsman"] == "BB McCullum":
                runs = runs + balls[ball]["runs"]["batsman"]

    return(runs)
