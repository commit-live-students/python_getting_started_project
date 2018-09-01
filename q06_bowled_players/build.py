# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    dta = data['innings'][1]['2nd innings']['deliveries']
    bowled_players =[]
    for i in range(len(dta)):
        key = list(dta[i].keys())[0]
        if 'wicket' in dta[i][key]:
            if dta[i][key]['wicket']['kind'] == 'bowled':
                bowled_players.append(dta[i][key]['batsman'])
    return bowled_players
dta = data['innings'][1]['2nd innings']['deliveries']
bowled_players =[]
for i in range(len(dta)):
    key = list(dta[i].keys())[0]
    if 'wicket' in dta[i][key]:
        if dta[i][key]['wicket']['kind'] == 'bowled':
            print(dta[i][key]['batsman'])
            bowled_players.append(dta[i][key]['batsman'])
print(data['innings'][1].keys())


