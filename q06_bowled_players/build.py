# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    for deliveries in [data['innings'][0]['1st innings']['deliveries'], data['innings'][1]['2nd innings']['deliveries']]:
        for delivery in deliveries:
            for delivery_number, delivery_info in delivery.items():
                if delivery_info.has_key('wicket') and delivery_info['wicket']['kind'] == 'bowled':
                    bowled_players.append(delivery_info['wicket']['player_out'])

    return bowled_players
