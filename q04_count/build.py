# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    first_inning = data['innings'][0]['1st innings']['deliveries']
    count = 0
    for balls in first_inning:
        for ball in balls:
            valid_balls = balls[ball]
            if valid_balls['batsman'] == 'RT Ponting':
                count += 1

    return count

print(deliveries_count(data))
