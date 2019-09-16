# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    second_innings_data = data['innings'][1]['2nd innings']['deliveries']
    for deliveries in second_innings_data:
        for players in deliveries:
            try:
                if deliveries[players]['wicket']['kind'] == 'bowled':
                    bowled_players.append(deliveries[players]['batsman'])
            except KeyError:
                pass
    return bowled_players


bowled_out(data)

