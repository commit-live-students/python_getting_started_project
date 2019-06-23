# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
bowled_players = []

# Your Solution
def bowled_out(data=data):

    # get the balls deliveries dictinoary for 2nd innings
    balls = data['innings'][1]['2nd innings']['deliveries']
    
    #initialize blank link


    #iterate through each ball in list
    for bal in balls:
        #iterate through each ball dictionary
        for bal_dict in bal.values():
            # check if wicket is a key in each ball diction
            if ('wicket' in bal_dict.keys()) and (bal_dict['wicket']['kind'] == 'bowled'):
                bowled_players.append(bal_dict['wicket']['player_out'])
            else:
                pass

    return bowled_players

if __name__ == '__main__':
    bowled_out()
    print(bowled_out())



