# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    extra_1 = 0
    extra_2 = 0

    deliveries1 = data["innings"][0]["1st innings"]["deliveries"]
    deliveries2 = data["innings"][1]["2nd innings"]["deliveries"]

    for delivery1 in deliveries1:
        for delivery1_num, delivery1_info in delivery1.items() :
            if "extras" in delivery1_info.keys() :
                extra_1 = extra_1 + 1

    for delivery2 in deliveries2:
        for delivery2_num, delivery2_info in delivery2.items() :
            if "extras" in delivery2_info.keys() :
                extra_2 = extra_2 + 1

    diff = extra_2 - extra_1

    return diff
