# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players=[]
    slices_1=[]
    print(data.keys())
    slices=(data['innings'][1]['2nd innings']['deliveries'])
    for a in slices:
        for b in a:
            if 'wicket' in a[b].keys():
                if(a[b]['wicket']['kind']=='bowled'):
                    bowled_players.append(a[b]['wicket']['player_out'])



    return bowled_players

#print(bowled_out())
