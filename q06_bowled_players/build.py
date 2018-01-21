# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    for i in range(0,len(data['innings'][1]['2nd innings']['deliveries'])):
        keys1 = data['innings'][1]['2nd innings']['deliveries'][i].keys()[0]
        if 'wicket' in data['innings'][1]['2nd innings']['deliveries'][i][keys1].keys():
            if data['innings'][1]['2nd innings']['deliveries'][i][keys1]['wicket']['kind'] == 'bowled':
                bowled_players.append(data['innings'][1]['2nd innings']['deliveries'][i][keys1]['batsman'])

    return bowled_players
