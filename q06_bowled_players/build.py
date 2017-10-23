# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here


    return bowled_players
runs = 0
for balls in data['innings'][0]['1st innings']['deliveries']:
    for key, value in balls.items():
        print value['wicket']
