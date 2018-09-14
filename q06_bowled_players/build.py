# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here

    bowled_players = []
    varfin2=data['innings'][1]['2nd innings']['deliveries']
    for indict in varfin2:
        for j,k in indict.items():
            for l,m in k.items():
               if ((l == 'wicket') and (m['kind'] == 'bowled')):
                   bowled_players.append(str(k['batsman']))

    return bowled_players

bowled_out(data)


