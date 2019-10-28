# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution

def bowled_out(data=data):
    bowled_players = []
    for deliveries in data['innings'][1]['2nd innings']['deliveries']:
        for delivery in deliveries:
            if 'wicket' in deliveries[delivery] and deliveries[delivery]['wicket']['kind'] == 'bowled':
                bowled_players.append(deliveries[delivery]['batsman'])
    return bowled_players
bowled_out()
