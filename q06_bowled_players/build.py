# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data):
    
    #assign a with avlues of data which would remain static throughout the problem statement
    a = data['innings'][1]['2nd innings']['deliveries']#[7][1.1]['wicket']['kind']  #For testing to access subsequent element.
    #print(type(a))
    #print(a)
    bowled_players=[]        #To store return data
    
    for i,v in enumerate(a):    #looping thru deliveries
        for k,v in a[i].items():   #looping thru deliveries viz. 0.1, 0.2 etc.
            if  'wicket' in a[i][k].keys():     #narrowing down in dicts which have 'wicket' as key.
                if 'bowled' in a[i][k]['wicket']['kind']:       #further filtering to narrow dewn on 'bowled' as kind of wicket.
                    #print(a[i][k]['wicket']['kind'],' ',a[i][k]['wicket']['player_out'])  # just to check the player names who were bowled out.
                    bowled_players.append(a[i][k]['wicket']['player_out'])

    return bowled_players


bowled_out(data)



