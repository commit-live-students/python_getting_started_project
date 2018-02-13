# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


def bowled_out(data=data):
    bowled_players=[]
    deliveries=data['innings'][1]['2nd innings']['deliveries']

    for deliveries in deliveries:
        for rounds in deliveries:
            if deliveries[rounds].get('wicket'):
                wicket=deliveries[rounds].get('wicket')

                for k,v in wicket.items():
                    if 'bowled' in v:
                        players=wicket.get('player_out')
                        bowled_players.append(players)
    return bowled_players
