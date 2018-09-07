# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    second_innings = data['innings'][1].get('2nd innings').get('deliveries')
    bowled_players =  []
    
    for x in range(0,len(second_innings)):
        delivery = second_innings[x]
        
        for key in delivery:
            if delivery[key].get('wicket') != None:
                
                if delivery[key].get('wicket').get('kind') == 'bowled':
                    bowled_players.append(delivery[key].get('batsman'))
    
    return bowled_players

