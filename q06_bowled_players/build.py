# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    dat = data['innings'][1]['2nd innings']['deliveries']
    for i in list(range(len(dat))):
        for key in dat[i]:
            if 'wicket' in dat[i][key] != None :
                if dat[i][key]['wicket']['kind'] == 'bowled' :
                 bowled_players == bowled_players.append(dat[i][key]['wicket']['player_out'])

    return bowled_players

bowled_out()




