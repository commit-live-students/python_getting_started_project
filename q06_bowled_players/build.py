# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    delivery = data['innings'][1]['2nd innings']['deliveries']
    bowled_players=[]
    for i in delivery:
        for key in i:
            x=i[key]
            if 'wicket' in x and x['wicket']['kind']=='bowled':
                bowled_players.append(x['batsman'])
    return bowled_players



