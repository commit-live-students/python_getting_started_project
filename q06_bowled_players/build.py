# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

bowled_players = []

# Your Solution
def bowled_out(data=data):

    # Write your code here
    for d in data['innings'][1]['2nd innings']['deliveries']:
        for ball in d.keys():
            if('wicket' in d[ball].keys()):
                # print(d[ball]['wicket'])
                if(d[ball]['wicket']['kind'] == 'bowled'):
                    print(d[ball]['wicket']['player_out'])
                    bowled_players.append(d[ball]['wicket']['player_out'])

    return bowled_players

bowled_out(data)
bowled_players


