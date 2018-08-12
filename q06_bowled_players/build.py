# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players=[]
    wickets=[]
    name=data['innings'][1]['2nd innings']['deliveries']
    for delivery in name:
        for delivery_number,delivery_info in delivery.items():
            if 'wicket' in delivery_info:
                ab=delivery.items()
                for anum,ainfo in ab:
                    wickets.append(ainfo['wicket'])
#                     for wnumber,winfo in wickets:
#                         print(winfo)
#                         if winfo['kind']=='bowled':
#                             bowled_players.append(winfo['batsman'])
    print(wickets)
    for i in range(len(wickets)):
        if wickets[i]['kind'] == 'bowled':
            bowled_players.append(wickets[i]['player_out'])
    return bowled_players
bowled_out(data)


