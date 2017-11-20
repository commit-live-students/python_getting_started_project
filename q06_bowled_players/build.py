# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here

    bowled_players = []

    for innings in range(len([data][0]['innings'])):
        for inn_name, inn_details in [data][0]['innings'][innings].items():
            for attr_name, del_info in inn_details.items():
                if attr_name <> 'team':
                    for del_details in del_info:
                        for delivery, delivery_outcome in del_details.items():
                            if 'wicket' in delivery_outcome and delivery_outcome['wicket']['kind'] == 'bowled':
                                bowled_players.append(delivery_outcome['wicket']['player_out'])

    return bowled_players
