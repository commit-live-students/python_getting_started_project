# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players=list()
    lst1=data['innings'][1]['2nd innings']['deliveries']
    for i,e in enumerate(lst1):
        for k in lst1[i].keys():
            if 'wicket' in lst1[i][k].keys():
                isbowled=lst1[i][k]['wicket']['kind']
                if isbowled=='bowled':
                    bowled_players.append(lst1[i][k]['wicket']['player_out'])
        

    return bowled_players


