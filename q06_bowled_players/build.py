# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    dely = data['innings'][1]['2nd innings']['deliveries']
    loop_var = 0
    bowled_players = []
    for batsman in dely:
        ind = data['innings'][1]['2nd innings']['deliveries'][loop_var].keys()
        wicket_or_not = data['innings'][1]['2nd innings']['deliveries'][loop_var][ind[0]].keys()
        if wicket_or_not[len(wicket_or_not) - 1] == 'wicket':
            if data['innings'][1]['2nd innings']['deliveries'][loop_var][ind[0]]['wicket']['kind'] == 'bowled':
                bowled_players.append(data['innings'][1]['2nd innings']['deliveries'][loop_var][ind[0]]['batsman'])

        loop_var=loop_var + 1

    return bowled_players

bowled_out()
