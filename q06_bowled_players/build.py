# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    a=[]
    for i in deliveries:
        for delivery , delivery_info in i.items() :
            a.append(delivery_info.get('wicket'))

    b = []
    for i in a:
        if i != None:
            b.append(i)

    bowled_players = []

    for i in b:
        if i['kind'] == 'bowled':
            bowled_players.append(i['player_out'])

    


    return bowled_players
