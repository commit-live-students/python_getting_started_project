# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    deliv=data['innings'][1]['2nd innings']['deliveries']
    # Write your code here
    d=list()
    bowled_players = list()
    d=list()
    count = 0
    for i in range(len(deliv)):
        d.append(deliv[i].items()[0][0])

    for i in range(len(deliv)):
        temp = d[i]
        if(deliv[i][temp].has_key('wicket')):
            if (deliv[i][temp]['wicket']['kind'] == 'bowled'):
                bowled_players.append(deliv[i][temp]['wicket']['player_out'])

    return bowled_players
