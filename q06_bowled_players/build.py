# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    type = ''
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    
    for delivery in deliveries:
        ballIndex = list(delivery.keys())[0]
        ball = delivery[ballIndex]
        
        if('wicket' in ball):
            wicketType = ball['wicket']['kind']
            if( wicketType == 'bowled'):
                batsman = ball['wicket']['player_out']
                bowled_players.append(batsman)
    
    return bowled_players

bowled_out(data=data)


