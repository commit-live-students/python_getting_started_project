# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    #print(deliveries)
    bowled_players = []
    for each_delivery in deliveries:
        for deliveryNumber, deliveryInfo in each_delivery.items():
            #print(deliveryInfo)
            if 'wicket' in deliveryInfo:
                if deliveryInfo['wicket']['kind'] == 'bowled':
                    bowled_players.append(deliveryInfo['batsman'])

    #print(bowled_players)
    return bowled_players
