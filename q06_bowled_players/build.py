# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    first_innings = data['innings'][0]['1st innings']['deliveries']
    second_innings = data['innings'][1]['2nd innings']['deliveries']
    deliveries = first_innings + second_innings
    bowled= [d.values()[0]['batsman'] for d in deliveries if 'wicket' in d.values()[0] and d.values()[0]['wicket']['kind'] =='bowled']
    bowled_players.extend(bowled)
    return bowled_players
