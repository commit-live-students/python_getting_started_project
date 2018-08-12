# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    
    for ball in range (len(data['innings'][1]['2nd innings']['deliveries'])):
        ball_number = list(data['innings'][1]['2nd innings']['deliveries'][ball].keys())[0]
        if 'wicket' in (data['innings'][1]['2nd innings']['deliveries'][ball][ball_number].keys()):
            if (data['innings'][1]['2nd innings']['deliveries'][ball][ball_number]['wicket']['kind']) == 'bowled':
                bowled_players.append((data['innings'][1]['2nd innings']['deliveries'][ball][ball_number]['batsman']))
    


    return bowled_players





