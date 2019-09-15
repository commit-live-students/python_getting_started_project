import yaml# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    path = './data/ipl_match.yaml'
    with open(path, mode = 'r') as file_loader:
        data = yaml.load(file_loader)
    count = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    # write your code here
    for balls in deliveries:
        for b in balls:
            if balls[b]['batsman'] == 'RT Ponting':
                count += 1
    # countYouforr code here
    return count
