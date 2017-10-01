# default imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))

from q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):

    # write your code here
    teams = data['info']['teams']

    return teams
