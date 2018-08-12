# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    bowled_players=[]
    deliveries=data['innings'][1]['2nd innings']['deliveries']
    #print(deliveries)
    for delivery in deliveries:
        (k, v), = delivery.items()

        current_wicked=v.get('wicket')
        if(current_wicked!=None):
            if((current_wicked['kind'])=='bowled'):
                #bowled_players+=1
                bowled_players.append(v['batsman'])

    # Write your code here


    return bowled_players


#bowled_out(data)
