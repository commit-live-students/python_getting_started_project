# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    deliveries_list=data["innings"][0]["1st innings"]["deliveries"]
    run=0
    for target_list in deliveries_list:
     for overs in target_list:
        if "BB McCullum"==target_list[overs]["batsman"]:

            if target_list[overs]["runs"]["batsman"]!=0:
                run=run+target_list[overs]["runs"]["batsman"]

    return run
