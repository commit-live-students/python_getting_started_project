# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
global count
# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    count=0
    deliveries_data=data["innings"][0]["1st innings"]["deliveries"]
    for i in range(0, len(deliveries_data)-1):
            keys=deliveries_data[i].keys()
            if (deliveries_data[i][keys[0]]["batsman"]) == "RT Ponting":
                count+=1

    return count
