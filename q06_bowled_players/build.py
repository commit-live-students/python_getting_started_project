# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players=[]
    # Write your code here
    for delivery in data['innings'][1]['2nd innings']['deliveries']:
        for key, val in delivery.items():
            if 'wicket' in val:
                if(val['wicket']['kind'] == 'bowled'):
                    bowled_players.append(val['batsman'])
    return bowled_players

bowled_out(data)
