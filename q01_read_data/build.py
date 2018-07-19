# %load q01_read_data/build.py
import yaml
def read_data():
    data = yaml.load(open('../data/ipl_match.yaml'))
    return data



