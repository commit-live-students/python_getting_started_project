# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    bowled_players = []
    for balls in data['innings'][1]['2nd innings']['deliveries']:
        for key,values in balls.items():
            try:
                new_value = values['wicket']
                if new_value['kind'] =="bowled":
                #print (new_value['player_out'])
                    bowled_players.append(new_value['player_out'])
            except KeyError:
        # Key is not present
                pass
    return  bowled_players
