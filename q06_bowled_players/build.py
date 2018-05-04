# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    bowled_players=[]
    for delivery in deliveries:
        delivery_t = list(delivery.values())
        for k,v in delivery_t[0].items():
            if 'wicket' in k:
                if delivery_t[0]['wicket']['kind']=='bowled':
                    bowled_players.append(delivery_t[0]['wicket']['player_out'])
    return bowled_players



