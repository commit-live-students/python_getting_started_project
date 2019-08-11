# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):

    # write your code here
    iplteams =data['info']['teams']

    return iplteams
