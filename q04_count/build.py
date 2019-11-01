# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    inn = data["innings"][0]["1st innings"]["deliveries"]
    count=0
    for i in range (0,len(inn)):
        delv = inn[i]
        if delv[delv.keys()[0]]['batsman'] == 'RT Ponting':
            count=count+1
    return count
