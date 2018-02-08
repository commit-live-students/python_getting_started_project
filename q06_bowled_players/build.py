# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players=[]
    d2= data['innings'][1]['2nd innings']['deliveries']
    l2=len(d2)
    for i in range(0,l2):
        k2=d2[i].keys()
        if ('wicket' in d2[i][k2[0]]) and ((d2[i][k2[0]]['wicket']['kind']) == 'bowled'):
            bowled_players.append(d2[i][k2[0]]['wicket']['player_out'])
    return bowled_players
