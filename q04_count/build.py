# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    ricky_ponting_balls_faced = []
    deliveries = data['innings'][0]['1st innings']['deliveries']

    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['batsman'] == 'RT Ponting':
                over_and_ball_number = delivery_number
        #             runs_scored = delivery_info['runs']['batsman']

                ricky_ponting_balls_faced.append((over_and_ball_number))

    count = len(ricky_ponting_balls_faced)
    return count
