# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    count = data['innings'][0]['1st innings']['deliveries']
    counter=0

    for i in count:
        sub_list=i.values()
        if sub_list[0]['batsman'] == 'RT Ponting':
            counter=counter + 1
    return counter

no_of_delivery = deliveries_count(data)
