# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data):

    # Write your code here
    bowled_players = []
    innings = data['innings']
    second_innings = innings[1]
    deliveries = second_innings['2nd innings']['deliveries']
    for item in deliveries:
        for k, v in item.items():
            if('wicket' in v):
                if(v['wicket']['kind'] == 'bowled'):
                    bowled_players.append(v['wicket']['player_out'])

    return bowled_players

bowled_out(data)

