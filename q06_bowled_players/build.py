# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    
    #Write your code here
    l=(data['innings'][1]['2nd innings']['deliveries'])
    c=[]
     
    for x in l:
        for y in x:
            if 'wicket' in x[y]:
                   
                if 'bowled' in x[y]['wicket']['kind']:
                    print(x[y]['wicket']['player_out'])
                        
                    c.append(x[y]['wicket']['player_out'])
            
    bowled_players=c
    return bowled_players
    


        
                                            
                                                               
bowled_out


