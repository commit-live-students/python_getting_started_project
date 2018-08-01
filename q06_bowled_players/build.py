# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for x in deliveries:
        listd = list(x.values())
        if 'wicket' in listd[0].keys():
            if (listd[0]['wicket']['kind']=='bowled'):
                bowled_players.append(listd[0]['batsman'])
        
    return bowled_players

# Items in the second set but not the first:                  |
# |                              |         | 'Z Khan'                                                    |
# |                              |         | 'V Kohli'                                                   |
# |                              |         | 'R Dravid' : The Expected Value does not match return value |

# print(data)
bowled_out()
# print(data['innings'][1]['2nd innings']['deliveries'])



