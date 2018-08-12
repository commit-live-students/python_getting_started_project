# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players=[]
    # Write your code here
    
    batsman=data['innings'][1]['2nd innings']['deliveries']
    for i in range(0,len(batsman)):
        for j in (batsman[i].keys()):
            if 'wicket' in (batsman[i][j]):
                if batsman[i][j]['wicket']['kind']=='bowled':
                    bowled_players.append(batsman[i][j]['wicket']['player_out'])
    return bowled_players
bowled_out(data)

