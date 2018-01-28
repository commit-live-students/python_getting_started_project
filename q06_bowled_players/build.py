# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_batsman = []
    second_inning = data['innings'][1]['2nd innings']['deliveries']
    for balls in second_inning:
        for ball in balls:
            delivery = balls[ball]
            if 'wicket' in delivery.keys():
                wicket_delivery = delivery['wicket']
                if wicket_delivery['kind'] == 'bowled':
                    players = delivery['batsman']
                    bowled_batsman.append(players)
                else:
                    pass

    return bowled_batsman
