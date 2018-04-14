# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    
    for balls in data['innings'][1]['2nd innings']['deliveries']:
        if 'wicket' in balls[list(balls.keys())[0]]:
            #print(balls[list(balls.keys())[0]]['wicket'])
            if balls[list(balls.keys())[0]]['wicket']['kind'] == 'bowled':
                bowled_players.append(balls[list(balls.keys())[0]]['wicket']['player_out'])
        
    return bowled_players
bowled_out(data)

