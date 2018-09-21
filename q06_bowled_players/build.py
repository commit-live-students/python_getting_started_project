# %load q06_bowled_players/build.py
# Default Imports
import pandas as pd
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    list_deliveries=data['innings'][1]['2nd innings']['deliveries']
    count=0
    bowled_players=[]
    
    for delivery in list_deliveries:
        for delivery_key,delivery_info in delivery.items():
            for subkey,subinfo in delivery_info.items():
                if subkey == 'wicket':
                    if subinfo['kind'] == 'bowled':
                        bowled_players.append(subinfo['player_out'])
                    
    print(bowled_players)
    
    return bowled_players


