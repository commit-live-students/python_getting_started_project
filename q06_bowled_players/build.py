# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # bowled_players = []
    bowled_players = []
    temp_1 = data.get('innings', {})
    temp_2 = temp_1[1]['2nd innings']['deliveries']
    for t in temp_2:
        for s in t:
             if 'wicket' in t[s] :
                if 'bowled' in t[s]['wicket']['kind']:
                    bowled_players.append(t[s]['wicket']['player_out'])
                    

                   



    return bowled_players

bowled_out()


