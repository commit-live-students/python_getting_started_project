# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    innings2 = data['innings'][1]['2nd innings']['deliveries']
    # Write your code here
    bowled_players = []
    for balls in innings2:
        for ball in balls.values():
            if 'wicket' in ball.keys():

                if ball['wicket']['kind']=='bowled':
                    bowled_players.append(ball['wicket']['player_out'])

    return bowled_players
