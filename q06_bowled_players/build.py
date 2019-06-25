# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    
    bowled_players=[]
    second_innings=data['innings'][1]['2nd innings']
    deliveries=second_innings['deliveries']
    for delivery in deliveries:
        for index in delivery :
            if(delivery[index].get('wicket')):  
                if delivery[index]['wicket']['kind']=='bowled':
                    bowled_players.append(delivery[index]['wicket']['player_out'])


    return bowled_players




