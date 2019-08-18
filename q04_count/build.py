# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    ball = []
    dd1 = data['innings'][0]['1st innings']['deliveries']
    for delivery in dd1:
        for delivery_number , delivery_info in delivery.items():
            if delivery_info['batsman'] == 'RT Ponting':
                over_and_ball_number = delivery_number
                ball.append(over_and_ball_number)
    count = len(ball)

    return count
