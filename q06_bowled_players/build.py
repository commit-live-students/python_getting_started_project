# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
def bowled_out(data=data):
    find1=data['innings'][1]['2nd innings']['deliveries']
    bowled_players=[]
    for i in find1:
        if i.values()[0].get('wicket') != None:
            if i.values()[0]['wicket']['kind']=='bowled':
                bowled_players.append(i.values()[0]['wicket']['player_out'])
    return bowled_players 
