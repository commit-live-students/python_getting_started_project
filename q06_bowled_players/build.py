# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players=[]
    for e in data['innings'][1]['2nd innings']['deliveries']:
        for key,element in e.items():
            if 'wicket' in e[key]:
                if e[key]['wicket']['kind']=='bowled':
                    bowled_players.append(e[key]['batsman'])
    # Write your code here


    return bowled_players
bowled_players=[]
for e in data['innings'][1]['2nd innings']['deliveries']:
    for key,element in e.items():
        if 'wicket' in e[key]:
            if e[key]['wicket']['kind']=='bowled':
                bowled_players.append(e[key]['batsman'])
                print(key,e[key]['batsman'],e[key]['wicket']['kind'])
                print(bowled_players)


