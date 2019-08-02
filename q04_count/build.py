# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for ball in deliveries:
        for each_ball in ball.values():
            if each_ball['batsman'] == 'RT Ponting':
                count += 1


    return count
