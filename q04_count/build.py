# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count = 0
    deliveries_faced =data["innings"][0]["1st innings"]["deliveries"]
    for item in deliveries_faced:
        for val in item.values():
            if val["batsman"] == "RT Ponting":
                count = count +1

    return count
