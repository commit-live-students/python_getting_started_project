# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    # Write your code here
    bowled_players = []
    for deliveries in data['innings'][1]['2nd innings']['deliveries']:
        for delivery in deliveries:
            if 'wicket' in deliveries[delivery]:
                if deliveries[delivery]['wicket']['kind'] == 'bowled':
                    bowled_players.append( deliveries[delivery]['wicket']['player_out'])
    return bowled_players
