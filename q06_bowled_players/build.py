# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    for delivery in data['innings'][1]['2nd innings']['deliveries']:
        for delivery_number in delivery:
            if 'wicket' in delivery[delivery_number] and delivery[delivery_number]['wicket']['kind'] == 'bowled':
                bowled_players.append(delivery[delivery_number]['batsman'])


    return bowled_players
