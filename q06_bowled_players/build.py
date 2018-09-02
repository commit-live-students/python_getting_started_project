# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players=[]
    for a in data['innings'][1]['2nd innings']['deliveries']:
            for b in a.values():
                for c in b.items():
                    if isinstance(c[1],dict):
                        for d in c[1].items():
                            if d[0]=='kind':
                                bowled_players.append(d[1])
                            print(bowled_players)
    return bowled_players

