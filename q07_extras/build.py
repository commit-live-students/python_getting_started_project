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

    for delivery in deliveries1:
        for delivery_num, delivery_info in delivery.items() :
            extra_1 = extra_1 + delivery_info["runs"]["extras"]

    for delivery in deliveries2:
        for delivery_num, delivery_info in delivery.items() :
            extra_2 = extra_2 + delivery_info["runs"]["extras"]

    difference = extra_2 - extra_1
    print difference
    return difference
