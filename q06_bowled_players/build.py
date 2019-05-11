# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution

def bowled_out(data=data):
    bowled_players=[]
    for k in data['innings'][1]['2nd innings']['deliveries']:
        for y,x in k.items():
            if 'wicket' in x :
                if x['wicket']['kind']== 'bowled':
                    i=x['batsman']
                    bowled_players.append(i)
    return bowled_players
#data['innings'][1]['2nd innings']['deliveries'][14]['2.2']['wicket']
