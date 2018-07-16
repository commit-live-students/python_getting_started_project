# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    # Your code here
    deliveries_list=data["innings"][0]["1st innings"]["deliveries"]
    count=0
    for target_list in deliveries_list:
     for overs in target_list:
        if "RT Ponting"==target_list[overs]["batsman"]:
            count=count+1

    return count
