# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here

    bowled = 0
    out = 0
    bowled_players = []
    delivery = data['innings'][1]['2nd innings']['deliveries']#[1]['2nd inning']['deliveries']
    for pl1 in range(len(delivery)):
        player = data['innings'][1]['2nd innings']['deliveries'][bowled].keys()
        bowled_pl = delivery[bowled][player[0]]
        if 'wicket' in bowled_pl:
            if delivery[bowled][player[0]]['wicket']['kind'] == 'bowled':
                bowled_players.append(data['innings'][1]['2nd innings']['deliveries'][bowled][player[0]]['batsman'])

        #print bowled_pl
        bowled += 1

    return bowled_players
print bowled_out()
