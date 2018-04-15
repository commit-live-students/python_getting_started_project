# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players=[]
    deliveries= data['innings'][1]['2nd innings']['deliveries']
    for d in deliveries:
        for key,value in d.items():
            if 'wicket' in value.keys():
                if value['wicket']['kind']=='bowled':
                    bowled_players.append(value['wicket']['player_out'])


    return bowled_players

bowled_out(data)

