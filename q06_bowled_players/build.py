# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    del_list = []
    del_list = data['innings'][1]['2nd innings']['deliveries']
    bowled_players = []
    del_dict = {}
    wicket_dict = {}
    for i in del_list:
        del_dict = i
        for key, value in del_dict.items():
            wicket_dict = value
            if 'wicket' in wicket_dict:
                if(wicket_dict['wicket']['kind'] == 'bowled'):
                    bowled_players.append(wicket_dict['wicket']['player_out'])
    
    return bowled_players


