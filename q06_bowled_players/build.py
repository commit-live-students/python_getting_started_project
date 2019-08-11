# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    deliveries = data['innings'][1]['2nd innings']['deliveries']

    for i in deliveries:
        deliver = i.values()
        #print balls
        for x in deliver:
            ball = x
           #so far dict
            for type in ball:

                if type == 'wicket' and ball[type]['kind'] == 'bowled':
                    bowled_players.append(ball['batsman'])


    return bowled_players
