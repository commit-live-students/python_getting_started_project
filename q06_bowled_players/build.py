# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players=[]
    inf=data['innings'][1]
    for k,v in inf.items():
        for delivery in v['deliveries']:
            for a,b in delivery.items():
                if 'wicket' in b.keys():
                       ### if b['wicket']['kind']=='caught':
                        ###    bowled_players.append([b['wicket']['player_out']])
                    if(b['wicket']['kind'])=='bowled':
                            bowled_players.append(b['wicket']['player_out'])
                            
            
                    
                       
                    
    # Write your code here


    return bowled_players

bowled_out()


