# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    a=data['innings'][1]['2nd innings']['deliveries']
    # Write your code h
    bowled_players=[]
    for i in range(len(a)):
        for j in a[i].values():
            for k in j.items():
                if k[0]=='wicket':
                    #for l,v in k[1].items():
                        #print(l,v)
                    for x in k[1]:
                        if k[1]['kind']=='bowled':
                            bowled_players.append(k[1]['player_out'])
    return list(set(bowled_players))                  
                    
c=bowled_out(data)
c


