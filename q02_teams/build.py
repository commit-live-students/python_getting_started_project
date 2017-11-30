# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):
    f = data.values()
    fset = f[0]
    fset = fset.values()
    teams = fset[6]
    return teams
