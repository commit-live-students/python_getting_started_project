# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    for d in data['innings'][1]['2nd innings']['deliveries']:
        for k, v in d.items():
            if v.get('wicket',{}).get('kind') == 'bowled':
                bowled_players.append(v['batsman'])

    return bowled_players
bowled_out(data)
