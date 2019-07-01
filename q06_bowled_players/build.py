# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    bowled_players = []
    deliveries =  data['innings'][1]['2nd innings'] 
    for d in deliveries['deliveries']:
        for n in d.values():
            if ('wicket' in n.keys()): 
                if(n['wicket']['kind'] == 'bowled'):
                    bowled_players.append(n['batsman'])


    return bowled_players

bowled_out()


