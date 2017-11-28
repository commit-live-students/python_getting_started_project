# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count=0
    teammate=data["innings"][0]["1st innings"]["deliveries"]
    for delivery in teammate:
        for key, value in delivery.items():
            if (delivery[key]["batsman"] == "RT Ponting"):
                count += 1

    return count
