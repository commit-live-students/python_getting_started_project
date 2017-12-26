# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
count =0
# Your Solution Here
def deliveries_count(data=data):
    deliveries = data['innings'][0]['1st innings']['deliveries']
    global count
    for item in deliveries:
        for key,values in item.items():
            if values['batsman']=='RT Ponting':
                count=count+1
    return count
