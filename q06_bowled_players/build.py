# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    for deliveries in data['innings'][1]['2nd innings']['deliveries']:
        for data in deliveries.values():
            for info in data.keys():
                if info == 'wicket':
                    if data['wicket']['kind'] == 'bowled':
                        bowled_players.append(data['wicket']['player_out'])


    return bowled_players
