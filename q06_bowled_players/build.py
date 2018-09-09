# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def bowled_out(data=data):
    l=(data['innings'][1]['2nd innings']['deliveries'])
    c=[]
    for x in l:
        for y in x:
            if 'wicket' in x[y].keys():
                if 'bowled' in x[y]['wicket']['kind']:
                    #print(x[y]['wicket']['player_out'])
                    c.append(x[y]['wicket']['player_out'])
           


    # Write your code here

    bowled_players=c
    return bowled_players
print (bowled_out(data))


