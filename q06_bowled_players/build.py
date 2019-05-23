# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    dt = data['innings'][1]['2nd innings']['deliveries']
    for i in range(len((dt))):
        x = dt[i].keys()
        if(("wicket" in dt[i][x[0]]) and (dt[i][x[0]]["wicket"]["kind"]=="bowled")):
            bowled_players.append(dt[i][x[0]]["wicket"]["player_out"])
    return bowled_players
bowled_out()
