# %load q01_read_data/build.py

import yaml

def read_data():
    file = './data/ipl_match.yaml'
    with open(file) as f:
        data = yaml.load(f)
        return data










