# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
bowled_players=[]
def bowled_out(data=data):

    delivery=data['innings'][1]['2nd innings']['deliveries']
    for index in range(len(delivery)):
        for key in delivery[index]:
            if 'wicket' in delivery[index][key].keys():
                if(delivery[index][key]['wicket']['kind']=='bowled'):
                    bowled_players.append(delivery[index][key]['batsman'])


    return bowled_players



