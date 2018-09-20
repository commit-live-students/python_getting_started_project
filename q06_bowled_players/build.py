# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    for delivery in data['innings'][1]['2nd innings']['deliveries']:
        for deli_num in delivery:
            if 'wicket' in delivery[deli_num] and delivery[deli_num]['wicket']['kind']=='bowled':
                   bowled_players.append(delivery[deli_num]['batsman'])
    return bowled_players
bowled_out()





