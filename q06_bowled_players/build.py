# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    for innings in data['innings']:
        for key,value in innings.items():
            for balls in value['deliveries']:
                for k, v in balls.items():
                    if 'wicket' in v and 'kind' in v['wicket']:
                        if v['wicket']['kind'] == 'bowled':
                            name =  v['wicket']['player_out']
                            bowled_players.append(name)

    return bowled_players
