# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players=[]
    for a in data['innings'][1]['2nd innings']['deliveries']:
       for b in a.items():
    #print (len(b[1]))
        if len(b[1])==5:
            if isinstance((b[1].get('wicket')),dict):
           #print(b[1].get('wicket'))
               if len (b[1].get('wicket'))==2: 
                a=b[1].get('wicket')
                bowled_players.append(a['player_out'])
            
                        
    return bowled_players

