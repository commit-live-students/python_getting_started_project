# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    for m in data['innings'][1]['2nd innings']['deliveries']:
        for x in m:
            if 'wicket' in m[x] and m[x]['wicket']['kind'] == 'bowled':
                bowled_players.append(m[x]['batsman'])
    

    return bowled_players
bowled_out()

