# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
bowled_players=[]
# Your Solution
def bowled_out(data=data):

    # Write your code here
    data1=data['innings'][1]['2nd innings']['deliveries']
    #print(data1)
    for i in data1:
        data2=list(i.values())
        if 'wicket' in data2[0].keys():
            if data2[0]['wicket']['kind']=='bowled':
                bowled_players.append(data2[0]['wicket']['player_out'])

    return bowled_players



