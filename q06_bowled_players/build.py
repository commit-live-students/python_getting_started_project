# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    
    r = data['innings'][1]['2nd innings']['deliveries']
    for d in r:
        for read_inside in d:
            if 'wicket' in d[read_inside].keys() == True:
                if d[read_inside]['wicket']['kind'] == 'bowled':
                    bowled_players = bowled_players + d[read_inside]['wicket']['player_out']

    # Write your code here


    return bowled_players
