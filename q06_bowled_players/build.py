from greyatomlib.python_getting_started.q01_read_data.build import read_data
from pprint import pprint

data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []

    deliveries1 = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries1:
        for key,value in delivery.items():
            for key,value in value.items():
                if key == 'wicket' and value['kind'] == 'bowled':
                    bowled_players.append(value['player_out'])

    deliveries2 = data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries2:
        for key,value in delivery.items():
            for key,value in value.items():
                if key == 'wicket' and value['kind'] == 'bowled':
                    bowled_players.append(value['player_out'])

    return bowled_players
