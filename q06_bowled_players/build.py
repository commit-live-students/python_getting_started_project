# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

#Your Solution
def bowled_out(bowled_players):

    # Write your code here

    x1 = data['innings']
    x2 = x1[1]
    x3 = x2['2nd innings']['deliveries']
    bowled_players = []
    for index, x in enumerate(x3):
        x4 = x3[index]
        for values in x4.values():
            x5 = values.get('wicket', 'NP')
            if x5 != 'NP' and x5['kind'] == 'bowled':
                bowled_players.append(x5['player_out'])
    return bowled_players


