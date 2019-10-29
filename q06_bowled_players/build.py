# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = [j.values()[0]['batsman'] for i in data['innings'] for j in i.values()[0]['deliveries'] for key, value in j.values()[0].items() if key=='wicket' and value['kind']=='bowled']


    return bowled_players
