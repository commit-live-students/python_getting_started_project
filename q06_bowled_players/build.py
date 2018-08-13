# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    for innings in data['innings']:
        for inning in innings:
            for delivery in innings[inning]['deliveries']:
                delivery_content = delivery[next(iter(delivery))]
                if 'wicket' in delivery_content:
                    wicket_content = delivery_content['wicket']
                    if wicket_content['kind'] == 'bowled':
                        bowled_players.append(wicket_content['player_out'])


    return bowled_players
