# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()




                        
                     
                            

# Your Solution
def bowled_out(data=data):

    bowled_players = []
    # Write your code here
    for k in data['innings'][1]['2nd innings']['deliveries']:
        for data['innings'][1]['2nd innings']['deliveries'] in k:
            for x in k[data['innings'][1]['2nd innings']['deliveries']]:
                if(x == 'wicket'):
                    if(k[data['innings'][1]['2nd innings']['deliveries']]['wicket']['kind'] == 'bowled'):
                        bowled_players.append(k[data['innings'][1]['2nd innings']['deliveries']]['wicket']['player_out'])


    return bowled_players




