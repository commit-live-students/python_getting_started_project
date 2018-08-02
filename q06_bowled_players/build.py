# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
bowled_players= []
# Your Solution
def bowled_out(data=data):
    bowled_players= []
    # Write your code here
    dely=data['innings'][1]['2nd innings']['deliveries']
    for key in dely:
        for key1, value1 in key.items():
            for key2, value2 in value1.items():
                if key2 == 'wicket'                :
                    for key3, value3 in value2.items():
                        if (key3 == 'kind') & (value3 == 'bowled'):
                            bowled_players.append(value2['player_out'])


    return bowled_players
bowled_out()

                    
        


