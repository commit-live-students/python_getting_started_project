# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
bowled_players=[]
# Your Solution
def bowled_out(data=data):

    # Write your code here
    global bowled_players

    for x in data['innings'][0]['1st innings']['deliveries']:
        for k,v in x.items():
            try:
                if(v['wicket']['kind']=='bowled'):
                    print(v['wicket']['player_out'])
                    cc=v['wicket']['player_out']
                    bowled_players.append(cc)
            except KeyError:
                # Key is not present
                pass
    for x in data['innings'][1]['2nd innings']['deliveries']:
        for k,v in x.items():
            try:
                if(v['wicket']['kind']=='bowled'):
                    print(v['wicket']['player_out'])
                    cc=v['wicket']['player_out']
                    bowled_players.append(cc)
            except KeyError:
                # Key is not present
                pass
    return bowled_players
hh=bowled_out()
hh
