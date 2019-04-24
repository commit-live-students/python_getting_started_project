# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    del_list = data['innings'][1]['2nd innings']['deliveries']
    #print del_list
    for i in range(0, len(del_list)):
        for k1, v1 in del_list[i].items():
            if 'wicket' in v1.keys():
                if(v1['wicket']['kind'] == 'bowled'):
                    player = v1['wicket']['player_out']
                    bowled_players.append(player)

    return bowled_players
print bowled_out(data)
