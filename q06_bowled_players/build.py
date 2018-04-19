# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def bowled_out(data=data):
    bowled_players = []
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if 'wicket' in delivery_info and delivery_info['wicket']['kind'] == 'bowled':
                bowled_players.append(delivery_info['wicket']['player_out'])

    return bowled_players

bowled= bowled_out(data)
print(bowled)




