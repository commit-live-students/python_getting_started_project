# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    deliveries = data["innings"][0]["1st innings"]["deliveries"]

    balls_faced_by_ponting =\
        [x for i in range(0, len(deliveries) - 1)
         for x in deliveries[i].values()
         if deliveries[i].values()[0]["batsman"] == "RT Ponting"]

    count = len(balls_faced_by_ponting)

    return count
