# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    deliveries = data["innings"][0]["1st innings"]["deliveries"]
    runs = sum(
        [v.values()[0]["runs"]["batsman"] for _, v in enumerate(deliveries)
         if v.values()[0]["batsman"] == "BB McCullum"]
        )
    return(runs)
