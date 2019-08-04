# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []

    innings = data['innings']
    for inning in innings:
        for delivery in inning.values()[0]['deliveries']:
            delivery = delivery.values()[0]
            if 'wicket' in delivery and delivery['wicket']['kind'] == 'bowled':
                bowled_players.append(delivery['batsman'])


    return bowled_players
