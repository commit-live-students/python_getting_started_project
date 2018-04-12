# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    bowled_players=list()
    
    maintemp = (data['innings'][1]['2nd innings']['deliveries'])
    len_maintemp = len(maintemp)
    
    for ctr in range(len_maintemp):
        temp_balls=(list(maintemp[ctr]))
        balls=float(temp_balls[0])
        
        if 'wicket' in maintemp[ctr][balls]:
            if maintemp[ctr][balls]['wicket']['kind'] == 'bowled':
                bowled_players.append(maintemp[ctr][balls]['wicket']['player_out'])
    
    return bowled_players
bowled_out(data)

