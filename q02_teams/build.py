# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):
    namesofteams=data['info']['teams']
    print type(namesofteams)
    return namesofteams

teams()
