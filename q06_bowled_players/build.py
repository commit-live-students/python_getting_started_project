# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    for x in data['innings'][1]['2nd innings']['deliveries']:
        for z,y in x.items():
            if 'wicket' in y:
                if y['wicket']['kind'] == "bowled":
                    bowled_players.append(y['batsman'])

    return bowled_players
