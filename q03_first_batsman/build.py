# %load q03_first_batsman/build.py
# Default Imports
import yaml
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):

    path = './data/ipl_match.yaml'
    with open(path, mode='r') as file_loader:
        data = yaml.load(file_loader)

    #name = data['innings']['1st innings']['deliveries'][0.1]['batsman']
    #name = data['innings'][0]['1st innings'][1]['deliveries'][0][0.1][0]['batsman']
    #name = data['innings'][0]['1st innings'][1]['batsman']
    name = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
    #name = 'SC Ganguly'
    return name


