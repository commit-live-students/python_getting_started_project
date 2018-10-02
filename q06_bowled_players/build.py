# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for x in deliveries:
        listd = list(x.values())
        if 'wicket' in listd[0].keys():
            if (listd[0]['wicket']['kind']=='bowled'):
                bowled_players.append(listd[0]['batsman'])

    # Write your code here


    return bowled_players




