# %load q01_read_data/build.py
import yaml

def read_data():
    file_path= './data/ipl_match.yaml'
    with open(file_path, 'r') as f:
        data = yaml.load(f)

    # return data variable
    return data








