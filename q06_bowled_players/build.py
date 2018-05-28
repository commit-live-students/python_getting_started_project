# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    deliveriesInSecond = data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveriesInSecond:
        for ball in delivery.keys():
            if 'wicket' in delivery[ball].keys():
                if(delivery[ball]['wicket']['kind'] == 'bowled'):
                    bowled_players.append(delivery[ball]['wicket']['player_out'])
    # Write your code here


    return bowled_players



