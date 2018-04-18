# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    ddata = data['innings'][1]['2nd innings']['deliveries']
    return [x[y]['batsman'] for x in ddata for y in x if 'wicket' in x[y] and x[y]['wicket']['kind'] == 'bowled']


[x[y]['batsman'] for x in data['innings'][1]['2nd innings']['deliveries'] for y in x if 'wicket' in x[y] and x[y]['wicket']['kind'] == 'bowled']   

for k in data['innings'][1]['2nd innings']['deliveries']:
    print (k)
    for data['innings'][1]['2nd innings']['deliveries'] in k:
        print 
    


