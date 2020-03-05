# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


def bowled_out(data=data):
    bowled_players = []
    a = data['innings'][1]['2nd innings']['deliveries']
    for deliveries in a:
        for ball in deliveries:
            if ('wicket' in deliveries[ball].viewkeys()) and (deliveries[ball]['wicket']['kind'] == 'bowled'):
                bowled_players.append(deliveries[ball]['wicket']['player_out'])
    #print bowled_players
    return bowled_players
print bowled_out()
