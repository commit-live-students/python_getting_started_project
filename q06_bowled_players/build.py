# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players=[]
    total_del_2nd_innings=len(data['innings'][1]['2nd innings']['deliveries'])
    lst=data['innings'][1]['2nd innings']['deliveries']
    for i in range(total_del_2nd_innings):
        for x,y in lst[i].items():
            if('wicket' in lst[i][x]) and (lst[i][x]['wicket']['kind']=='bowled'):
                bowled_players+=[lst[i][x]['wicket'].get('player_out')]
        
    return bowled_players
bowled_out()

