# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    
    bowled_players = [] #empty list for storing bowled players
    
    #total number of ball played in whole match
    number_of_balls_played = len(data['innings'][1]['2nd innings']['deliveries'])
    
    for ball_number in range(number_of_balls_played):
        
        #dictionary of each ball
        di = data['innings'][1]['2nd innings']['deliveries'][ball_number]
        
        for ke in di.keys(): # to get inside the ball details
            
            # check whether player out or not in particular ball
            if ( 'wicket' in data['innings'][1]['2nd innings']['deliveries'][ball_number][ke].keys()):
                
                # check wicket get was bowled 
                if data['innings'][1]['2nd innings']['deliveries'][ball_number][ke]['wicket']['kind'] == 'bowled':
                        
                        bowled_players.append(data['innings'][1]['2nd innings']['deliveries'][ball_number][ke]['wicket']['player_out'])

    return bowled_players

bowled_out(data)


