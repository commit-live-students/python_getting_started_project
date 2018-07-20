# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    # Write your code here
    l1 = data.get('innings')[1].get('2nd innings').get('deliveries')
    for s in l1:
        for key, value in s.items():
            myval = value
            if('wicket' in myval):
                if(myval.get('wicket').get('kind')=='bowled'):
                    name=str(myval.get('wicket').get('player_out'))         
                    bowled_players.append(name)        
                
    return bowled_players


bowled_out(data)


