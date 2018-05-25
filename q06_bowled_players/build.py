# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
bowled_players = []
# Your Solution
def bowled_out(data=data):

    # Write your code here
    lst1 = data['innings'][1]['2nd innings']['deliveries']
    for value in lst1:
        for k2,v2 in value.items():
            try:
                if v2['wicket']['kind']  == 'bowled':
                    bowled_players.append(v2['wicket']['player_out'])
            except KeyError:
                continue

        return bowled_players


