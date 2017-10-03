# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    bowled_players = []

    for delivery in deliveries:
        for over, info in delivery.items():
            if info.get('wicket') is not None :
                if ( info['wicket']['kind'] == 'bowled' ) :
                    bowled_players.append(info['wicket']['player_out'])

    return bowled_players
