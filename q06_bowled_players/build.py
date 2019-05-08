# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    # Write your code here
    bowled_players = []
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for d in deliveries:
        current_delivery = list(d)
        delivery_detail = d[current_delivery[0]]
        try:
            if(delivery_detail['wicket']):
                if(delivery_detail['wicket']['kind']=='bowled'):
                    boweled = delivery_detail['batsman']
                    bowled_players.append(boweled)
            
        except KeyError:
                pass
    return bowled_players

bowled_out(data)

