# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for x in deliveries:
        listtest = list(x.values())
        if 'wicket' in listtest[0].keys():
            if (listtest[0]['wicket']['kind']=='bowled'):
                bowled_players.append(listtest[0]['batsman'])
        
     # Write your code here
    return bowled_players


