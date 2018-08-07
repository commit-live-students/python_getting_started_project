# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players=[]
    for dict in data['innings'][1]['2nd innings']['deliveries']:
        for deliveries_dict in dict.values():
            if ('wicket' in deliveries_dict and deliveries_dict['wicket']['kind']=='bowled'):
                bowled_players.append(deliveries_dict['wicket']['player_out'])
            


    return bowled_players





