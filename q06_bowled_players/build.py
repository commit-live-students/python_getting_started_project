# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players=[]
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    # Write your code here
    
    for x in deliveries:
        for y in x:
            if 'wicket' in x[y]:
                if x[y]['wicket']['kind']=='bowled':
                    bowled_players.append(x[y]['wicket']['player_out'])

    return bowled_players




