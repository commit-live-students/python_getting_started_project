# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players=[]
    lst1=data['innings'][1]['2nd innings']['deliveries']
    for lst in lst1:
        ball_detail=lst
        for ball_number in ball_detail.keys():
            if('wicket' in ball_detail[ball_number].keys()):
                if(ball_detail[ball_number]['wicket']['kind']== 'bowled'):
                    bowled_players.append(ball_detail[ball_number]['wicket']['player_out'])
    return bowled_players

