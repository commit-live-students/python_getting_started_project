# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    bowled_players = []
    second_inning = data['innings'][1]['2nd innings']['deliveries']
    for deliveries in second_inning:
        for delivery in deliveries:
            ball_data = deliveries[delivery]
            if 'wicket' in ball_data:
                wicket_data = ball_data['wicket']
                if wicket_data['kind'] == 'bowled':
                    bowled_players.append(ball_data['batsman'])
    return bowled_players
