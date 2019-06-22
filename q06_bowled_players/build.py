# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for t in deliveries:
        for m in t:
            for n in t[m]:
                #print('n-->',n,'-->t[m][n]',t[m][n])
                #print(t[m][n]['kind'])
                if n == 'wicket':
                    for o in t[m][n]:
                        if(o =='kind') & (t[m][n][o]=='bowled'):
                            print('o ',t[m][n][o])
                            bowled_players.append(t[m][n]['player_out']) 
    return bowled_players



