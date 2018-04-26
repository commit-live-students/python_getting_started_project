# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()



# Your Solution
def bowled_out(data=data):

    bowled_out = data['innings'][1]['2nd innings']['deliveries']
    #print(bowled_out)

    bowled_players = []
    
    for i in bowled_out:
#         print(i)
        for ball,wicket in i.items():
#             print(wicket['wicket'])
            if 'wicket' in wicket and wicket['wicket']['kind']=='bowled':
#                 print(wicket['wicket']['player_out'])
                bp=wicket['wicket']['player_out']
                print(bp)
                bp= bowled_players.append(bp)
                
    return bowled_players
print(bowled_out())



