# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    for x in data['innings'][1]['2nd innings']['deliveries']:
        for y,v in x.items():
            for w,t in v.items():
                if w == 'wicket':
                    for d,m in t.items():
                        if m == 'bowled':
                            data = t['player_out']
                            bowled_players.append(data)


    return bowled_players
# bowled_players = ()
# for x in data['innings'][1]['2nd innings']['deliveries']:
#
#     for y,v in x.items():
#         for w,t in v.items():
#             if w == 'wicket':
#
#                 for d,m in t.items():
#                     if m == 'bowled':
#                          data = t['player_out']
#                          bowled_players.append(data)




#
