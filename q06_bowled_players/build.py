# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    total_balls = len(data['innings'][1]['2nd innings']['deliveries'])
    for i in range(0,total_balls):
        key = next(iter(data['innings'][1]['2nd innings']['deliveries'][i]))
        try:
            if data['innings'][1]['2nd innings']['deliveries'][i][key]['wicket']['kind'] == 'bowled':
                batsman = data['innings'][1]['2nd innings']['deliveries'][i][key]['wicket']['player_out']
                if batsman not in bowled_players: 
                    bowled_players.append(batsman)
        except KeyError:
            pass
    return bowled_players






