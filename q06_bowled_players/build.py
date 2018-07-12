# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    # Write your code here
    delivery = data['innings'][1]['2nd innings']['deliveries']
    for balls in delivery:
        data1 = list(balls.values())
        if 'wicket' in data1[0].keys():
            if data1[0]['wicket']['kind']=='bowled':
                bowled_players.append(data1[0]['batsman'])
    return bowled_players   

bowled_out(data)


            


