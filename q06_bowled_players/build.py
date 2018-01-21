# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    bowled_players = [v['wicket']['player_out'] for d in deliveries for k,v in d.items() if 'wicket' in v if v['wicket']['kind'] == 'bowled']

    return bowled_players
