# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    deliveries=data['innings'][0]['1st innings']['deliveries']
    count=0
    for balls in deliveries:
        if balls.values()[0]['batsman']=='RT Ponting':
            count=count+1


    return count
