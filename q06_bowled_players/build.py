# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    # Write your code here
    bowled_players = []
    sec_inn = data['innings'][1]['2nd innings']['deliveries']
    
    for b in sec_inn:
        for k in b:
            if ('wicket' in b[k].viewkeys()) and (b[k]['wicket']['kind'] == 'bowled'):
                bowled_players.append(b[k]['wicket']['player_out'])



    return bowled_players
bowled_out(data)


