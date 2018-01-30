# %load q01_read_data/build.py
import yaml

def read_data():

    path = './data/ipl_match.yaml'
    with open(path, mode='r') as file_loader:
        data = yaml.load(file_loader)

    # return data variable
    return data


