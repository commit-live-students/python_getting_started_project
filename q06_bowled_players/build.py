# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    first_inning = data['innings'][1]['2nd innings']['deliveries']
    for each_delivery in first_inning:
        for each_ball, each_ball_detail in each_delivery.items():
            if each_ball_detail.get('wicket', {}).get('kind') == 'bowled':
                bowled_players.append(each_ball_detail['batsman'])

    return bowled_players
bowled_out(data)
