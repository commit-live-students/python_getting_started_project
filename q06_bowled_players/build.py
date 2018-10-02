# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
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

l=(data['innings'][0]['1st innings']['deliveries'])
c=0
for x in l:
    for y in x:
        if(x[y]['batsman'])=='BB McCullum':
            c+=(x[y]['runs']['batsman'])
                
print(c)
(data['innings'][1]['2nd innings']['deliveries'][7][1.1]['wicket']['kind'])
v=(data['innings'][1]['2nd innings']['deliveries'][1][0.2])
v.get('wicket')
(data['innings'][1]['2nd innings']['deliveries'][7][1.1])
(data['innings'][1]['2nd innings']['deliveries'][1][0.2])
l=(data['innings'][1]['2nd innings']['deliveries'])
c=[]
for x in l:
    for y in x:
        if 'wicket' in x[y].keys():
            if 'bowled' in x[y]['wicket']['kind']:
                print(x[y]['wicket']['player_out'])
                c.append(x[y]['wicket']['player_out'])
           
print(c)
l=(data['innings'][1]['2nd innings']['deliveries'])
c=0
for x in l:
    for y in x:
        if 'wicket' in x[y].keys():
            print('yo')



