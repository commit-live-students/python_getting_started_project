# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    bowled_players = []
    req_data = data['innings'][1]['2nd innings']['deliveries']
    for i in req_data:
        overs = i.items()
        #print overs
        for ball in overs:
            if ((ball[1].get('wicket','Absent') != 'Absent') and (ball[1]['wicket']['kind'] == 'bowled')):
                bowled_players.append(ball[1]['batsman'])

    return bowled_players
