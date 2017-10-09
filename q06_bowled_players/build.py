# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players=[]
    # Write your code here
    test=data['innings'][1]['2nd innings']['deliveries']
#     print (test)

    for i in test:
        #print(i)
        for j in i.values():
            #print(j)
            if 'wicket' in j.keys():
                if(j['wicket']['kind']=="bowled"):
                    bowled_players.append(j['batsman'])

    return bowled_players



print(bowled_out(data))
            
