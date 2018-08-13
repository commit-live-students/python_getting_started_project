# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    # Write your code here
    bowled_players = []
    for k,v in data['innings'][1].iteritems():
		bowled_players = [e['batsman'] for i, x in enumerate(v['deliveries']) for e in x.values() if 'wicket' in e and e['wicket']['kind'] == 'bowled']
    return bowled_players
