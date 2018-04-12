# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    return [delivery_data[delivery]['batsman'] for delivery_data in deliveries for delivery in delivery_data if 'wicket' in delivery_data[delivery] and delivery_data[delivery]['wicket']['kind'] == 'bowled']


