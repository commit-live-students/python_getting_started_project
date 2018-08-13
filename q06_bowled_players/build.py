# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    for delivery in data['innings'][1]['2nd innings']['deliveries']:
        #print delivery.values()[0].keys()
        if 'wicket' in delivery.values()[0].keys():
            if delivery.values()[0]['wicket']['kind'] == 'bowled':
                bowled_players.append(delivery.values()[0]['wicket']['player_out'])
    return bowled_players
print bowled_out(data)
