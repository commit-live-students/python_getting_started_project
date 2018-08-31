# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players=[]
    deliv2 = data['innings'][1]['2nd innings']['deliveries']
    for d2 in deliv2:
        for d2_num, batsm2 in d2.items():
            if ('wicket' in batsm2):
            
                if batsm2['wicket']['kind']=='bowled':
                    print(batsm2['wicket']['kind'], batsm2['wicket']['player_out'])
                    bowled_players.append(batsm2['wicket']['player_out'])

    return bowled_players


            


