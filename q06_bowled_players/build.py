# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    # Write your code here
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries:
        for delivery_no,delivery_info in delivery.items():
            try:
                if(delivery_info['wicket']['kind']=='bowled'):
                    bowled_players.append(delivery_info['batsman'])
            except KeyError:
                pass
    return bowled_players
