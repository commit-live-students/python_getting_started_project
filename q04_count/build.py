# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count = 0
    delivs = data['innings'][0]['1st innings']['deliveries']
    for d in delivs:
        for ball_no, info in d.items():
            if info['batsman'] == 'RT Ponting':
                balls_faced = ball_no
                count += 1
    return count
