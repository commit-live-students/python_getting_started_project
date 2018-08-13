# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    # Write your code here
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries:
        for del_obj, del_info in delivery.items():
            if 'wicket' in del_info:
                if del_info['wicket']["kind"] == 'bowled':
                    bowled_players.append(del_info['batsman'])
    # Write your code here
    return bowled_players
