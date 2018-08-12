# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    delivery_list = data['innings'][1]['2nd innings']['deliveries']
    bowled_players = []
    #print (type(delivery_list))
    
    for delivery_detail in delivery_list:
        for delivery_detail_val in delivery_detail.values():
            for delivery_detail_values in delivery_detail_val:
                if(delivery_detail_values == 'wicket' and delivery_detail_val[delivery_detail_values]['kind'] == 'bowled'):
                    bowled_players.append(delivery_detail_val[delivery_detail_values]['player_out'])

    return bowled_players
bowled_out(data)

