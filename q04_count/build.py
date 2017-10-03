# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    innings1 = data['innings'][0]['1st innings']['deliveries']
    count = 0
    for ball in innings1:
        for ball_l in ball.values():
            if ball_l['batsman'] == 'RT Ponting':
                count+=1
    # Your code here


    return count
