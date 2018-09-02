# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players=[]
    for a in data['innings'][1]['2nd innings']['deliveries']:
            if data['innings'][1]['2nd innings']['deliveries'][a]['player_out']:
                bowled_players.extend(data['innings'][1]['2nd innings']['deliveries'][a]['player_out'].values)
    return bowled_players

