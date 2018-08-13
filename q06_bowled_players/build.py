# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    d = data['innings'][1]['2nd innings']['deliveries']
    my_list = [a[k] for a in d for k in a ]
    bowled_players = [x['batsman'] for x in my_list if 'wicket' in x and x['wicket']['kind'] == 'bowled']
    return bowled_players
