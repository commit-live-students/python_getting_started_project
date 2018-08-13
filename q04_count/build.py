# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
counter = []

# Your Solution
def deliveries_count(data=data):
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for deliver_val in delivery.values():
            if(deliver_val['batsman']=='RT Ponting'):
                ball_faced = 1
                counter.append (ball_faced)
    count = sum(counter)
    return(count)
