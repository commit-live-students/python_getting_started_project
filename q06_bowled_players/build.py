# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players=[]
    for delivery in data['innings'][1]['2nd innings']['deliveries']:
        if(delivery[next(iter(delivery))].get('wicket',{}).get('kind',None)=='bowled'):
            bowled_players.append(delivery[next(iter(delivery))]['batsman'])
            
    return bowled_players

a=bowled_out()
a


