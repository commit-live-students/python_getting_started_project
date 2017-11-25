# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):

    # write your code here
    teams = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
    return teams
