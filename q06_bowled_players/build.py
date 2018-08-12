# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled = []
    deliveries = data["innings"][1]["2nd innings"]["deliveries"]

    for delivery in deliveries :
        for delivery_num, delivery_info in delivery.items() :
            if "wicket" in delivery_info.keys() :
                if delivery_info["wicket"]["kind"] == "bowled" :
                    bowled.append(delivery_info["batsman"])

    print bowled

    return bowled
