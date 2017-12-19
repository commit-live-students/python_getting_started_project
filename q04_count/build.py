# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    data1 = data['innings'][0]['1st innings']['deliveries']
    nos_of_delivery = 0
    for i in data1:
        if i.values()[0]['batsman']=='RT Ponting':
            nos_of_delivery = nos_of_delivery+1
    return nos_of_delivery
