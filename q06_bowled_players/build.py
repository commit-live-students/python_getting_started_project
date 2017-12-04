# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for ball in deliveries:
        for each_ball in ball.values():
            for x in each_ball.keys():
                if x == 'wicket':
                    if each_ball[x]['kind'] == 'bowled':
                         bowled_players.append(each_ball['batsman'])

    return bowled_players
