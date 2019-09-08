# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    b = data['innings'][1]['2nd innings']['deliveries']
    for i in range(len(b)):
        for j in b[i]:
            for k in b[i][j]:
                if k == 'wicket':
                    if b[i][j][k]['kind'] == 'bowled':
                        bowled_players += [b[i][j][k]['player_out']]
    # Write your code here


    return bowled_players
