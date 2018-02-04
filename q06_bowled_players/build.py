# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    bowled_players=[]
    for k in data['innings'][1]['2nd innings']['deliveries']:
        for y,x in k.items():
            for 'wicket' in x:
                if x['wicket']['kind']=='bowled':
                    print 'a'
    #return bowled_players
