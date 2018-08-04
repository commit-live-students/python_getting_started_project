# %load q01_read_data/build.py
import yaml

def read_data():
    with open('./data/ipl_match.yaml') as stream:
        data = yaml.load(stream)

    # return data variable
    return data


