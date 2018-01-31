# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    bowled_players = []
    innings = data['innings']
    second_innings = innings[1]['2nd innings']
    deliveries = second_innings['deliveries']

    for k in deliveries:
        for key, value in k.iteritems():
            param = 'wicket'
            if param in value:
                if value['wicket']['kind']  == 'bowled':
                    bowled_players.append(value['wicket']['player_out'])

    return bowled_players
