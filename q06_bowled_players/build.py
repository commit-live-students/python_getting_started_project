# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
bowled_players=[]
def bowled_out(data=data):
    bowled_players=[]
    deliveries=data['innings'][1]['2nd innings']['deliveries']
    for del_access in deliveries:
        for x,y in del_access.items():
            for p,q in y.items():
                if p=='wicket':
                    if q['kind']=='bowled':
                        bowled_players.append(q['player_out'])
    return (bowled_players)

deliveries=data['innings'][1]['2nd innings']['deliveries']
for del_access in deliveries:
    for x,y in del_access.items():
            for p,q in y.items():
                if p=='wicket':
                    if q['kind']=='bowled':
                        bowled_players.append(q['player_out'])
print(bowled_players)

