# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players=[]
    batsman=data['innings'][1]['2nd innings']['deliveries']

    for n in batsman:
        for ele in n.values()[0].keys():
            if ele=='wicket':
                if n.values()[0]['wicket']['kind']=='bowled':
                    bowled_players.append(n.values()[0]['wicket']['player_out'])

    return bowled_players
