# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
#def bowled_out(data=data):

    # Write your code here
    
def bowled_out(data=data):
    bowled_players = []
    my_list = data['innings'][1]['2nd innings']['deliveries']
    for x in my_list:
        for key in x:
            var1 = x[key]
            for key2 in var1:
                if key2 == 'wicket':
                    key3 = var1[key2]
                    if key3['kind'] == 'bowled':
                        bowled_players.append(key3['player_out'])
    return bowled_players





