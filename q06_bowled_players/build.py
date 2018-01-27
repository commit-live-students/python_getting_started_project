# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    deliv = data['innings'][1]['2nd innings']['deliveries']

    for b in deliv:
        for k in b:
            if ('wicket' in b[k].viewkeys()) and (b[k]['wicket']['kind'] == 'bowled'):
                bowled_players.append(b[k]['wicket']['player_out'])


    return bowled_players
print bowled_out()
