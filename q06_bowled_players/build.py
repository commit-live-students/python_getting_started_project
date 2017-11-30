# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []

    data = data['innings']

    data = [i['2nd innings'] for i in data if '2nd innings' in i]
    
    data = [i['deliveries'] for i in data if 'deliveries' in i]

    for l in data[0]:
        for i in l:
            for j in l[i]:
                if j == 'wicket' and l[i][j]['kind'] == 'bowled':
                    bowled_players.append(l[i][j]['player_out'])

    return bowled_players
