# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    deliveries = data['innings'][1]['2nd innings']['deliveries']
# deliveries.items()
    for delivery in deliveries:
#      for delivery_number, delivery_info in delivery.items():
        for dele in delivery.values():
         wick = dele.get('wicket')
        if wick != None and wick['kind'] == 'bowled' :
#          if wick['kind'] is not None :
            bowled_players.append(wick['player_out'])

    return bowled_players

bowled_out(data)

