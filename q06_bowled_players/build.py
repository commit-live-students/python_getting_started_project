# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    bowled_players=[]

    deliveries=data['innings'][1]['2nd innings']['deliveries']
    for balls in deliveries:
        if 'wicket' in  balls.values()[0].keys():
            if balls.values()[0]['wicket']['kind']=='bowled':
                name=balls.values()[0]['batsman']
                bowled_players.append (name)



    return bowled_players
