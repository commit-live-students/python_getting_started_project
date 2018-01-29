# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):
    #solution
    info = data.get('info')
    teams = info.get('teams')
    return teams
