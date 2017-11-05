# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs = 0
    bc_total_runs = data["innings"][0]["1st innings"]["deliveries"]
    for item in bc_total_runs:
        for val in item.values():
            if val["batsman"] == "BB McCullum":
                #print val["runs"]["batsman"]
                runs = runs+val["runs"]["batsman"]

    return (runs)
