# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for i in deliveries:
        for x in i:
            run_var = i[x]
            if 'wicket' in run_var and run_var['wicket']['kind'] == 'bowled':
                bowled_players.append(run_var['batsman'])
    return bowled_players

    # Write your code here


    return bowled_players

bowled_out(data)


