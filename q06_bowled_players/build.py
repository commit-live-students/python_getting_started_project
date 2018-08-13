# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    deliv = data['innings'][1]['2nd innings']['deliveries']
    for d in deliv:
        for ball_no, info in d.items():
            for w, k in info.items():
                if w == 'wicket' and k['kind'] == 'bowled':
                    bowled_players.append(info['batsman'])

    return bowled_players
