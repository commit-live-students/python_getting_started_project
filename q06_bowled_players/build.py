# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players= []
    bowled = data['innings'][1]['2nd innings']['deliveries']
    for x in bowled:
        for y in x:
            if x[y].get('wicket'):
                if x[y]['wicket']['kind'] =='bowled':
                    bowled_players.append(x[y]['wicket']['player_out'])
    
    
    return bowled_players
    
bowled_out(data=data)



bowled_out(data=data)



