# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs=0


    for i in data["innings"][0]["1st innings"]["deliveries"]:

        for key in i:
            if i[key]["batsman"]=="BB McCullum":
                runs+=i[key]["runs"]["batsman"]





    return(runs)
