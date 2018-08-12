# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
global runs

# Your Solution
def BC_runs(data=data):

    # Write your code here
    runs=0
    deliveries_data=data["innings"][0]["1st innings"]["deliveries"]
    for i in range(0, len(deliveries_data)):
            keys=deliveries_data[i].keys()
            if (deliveries_data[i][keys[0]]["batsman"]) == "BB McCullum":
                runs+=deliveries_data[i][keys[0]]["runs"]["batsman"]

    return(runs)
