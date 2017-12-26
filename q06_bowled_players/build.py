# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
bowled_players=[]
# Your Solution
def bowled_out(data=data):
    global bowled_players
    deliveries=data['innings'][1]['2nd innings']['deliveries']
    for item in deliveries:
        for keys,values in item.items():
                if 'wicket' in values:
                    if values['wicket']['kind']=='bowled':
                        bowled_players.append(values['batsman'])
    return bowled_players
