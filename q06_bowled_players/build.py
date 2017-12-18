# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players= []
    batsman = data['innings'][1]['2nd innings']['deliveries']
    for rp in batsman:
        #print rp.values()[0].keys()['wicket']
        for ele in rp.values()[0].keys():
            if ele =='wicket':
                if rp.values()[0]['wicket']['kind'] == 'bowled':
                    bowled_players.append(rp.values()[0]['wicket']['player_out'])
    return bowled_players


bowled_out()
