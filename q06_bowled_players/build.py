# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    bowled_players = []
    print(type(bowled_players))
    for i in deliveries:
        for e in i.items():
            if e[1].get('wicket') is not None and e[1].get('wicket')['kind'] == 'bowled':
                bowled_players.append(e[1]['batsman'])

    #print(bowled_players)

    return bowled_players



        



