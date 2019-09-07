# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    count = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for d in deliveries:
        key = d.keys()[0]
        if d[key]['batsman'] == 'RT Ponting':
            count=count+1
    return count
