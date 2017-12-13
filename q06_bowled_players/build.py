# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    data1 = data['innings'][1]['2nd innings']['deliveries'][:]
    for n in data1:
        if 'wicket' in n.values()[0].keys():
            if n.values()[0]['wicket']['kind'] == 'bowled':
                bowled_players.append(n.values()[0]['batsman'])

    return bowled_players

print bowled_out()
print type(bowled_out())
