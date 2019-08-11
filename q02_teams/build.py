# default imports
import yaml
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):
    # write your code here
    #teams =

    team=data['info']['teams']
    return team
