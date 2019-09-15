import yaml# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):
    path = './data/ipl_match.yaml'
    with open(path, mode = 'r') as file_loader:
        data = yaml.load(file_loader)

    teams = data['info']['teams']
    # write your code here
    #teams =

    return teams
