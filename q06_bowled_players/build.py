# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    r = data['innings'][1]['2nd innings']['deliveries']
    for d in r:
        for read_inside in d:
            if d[read_inside].get('wicket'):
                player = d[read_inside].get('wicket')
                if player.keys()[0] == 'kind':
                    bowled_players.append(player.get('player_out'))
    return bowled_players
