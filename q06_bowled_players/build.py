# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    count = 0
    key_list=[]
    abc=[]
    
    for i in range(0,92,1):
        abc=[]
        abc =list(data['innings'][1]['2nd innings']['deliveries'][i].keys())
        key_list.append(abc[0])
        
    bowled_players=[]
    for i in range(0,92,1):
        list_temp=list(data['innings'][1]['2nd innings']['deliveries'][i][key_list[i]].keys())
        if 'wicket' in str(list_temp):
            if str(data['innings'][1]['2nd innings']['deliveries'][i][key_list[i]]['wicket']['kind'])=='bowled':
                bowled_players.append(str(data['innings'][1]['2nd innings']['deliveries'][i][key_list[i]]['wicket']['player_out']))
            

    return bowled_players



