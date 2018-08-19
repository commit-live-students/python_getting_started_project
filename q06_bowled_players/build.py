# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    
    # Write your code here
    deliveries = list(data['innings'][1]['2nd innings']['deliveries'])
    bowled_players = list()
    for delivery in deliveries:
        for deliv in delivery:
            if 'wicket' in delivery[deliv] and 'bowled' in delivery[deliv].get('wicket')['kind'] :
                bowled_players.append(delivery[deliv].get('wicket')['player_out'])
                
    return bowled_players




