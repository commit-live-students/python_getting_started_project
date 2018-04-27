# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    # Write your code here
    bowled_players=[]
    
    for dict3 in data['innings'][1]['2nd innings']['deliveries']:
        for k,v in dict3.items():
            if 'wicket' in v.keys():
                 if v['wicket']['kind']=='bowled':
                        bowled_players.append(v['wicket']['player_out'])
    return bowled_players

bowled_out()








