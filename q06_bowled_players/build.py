# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players=[]
    deliveries=data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries:
        for key in delivery:
            if 'wicket' in delivery[key]:
                if delivery[key]['wicket']['kind']=='bowled':
                    bowled_players.append(delivery[key]['wicket']['player_out'])
    return bowled_players



