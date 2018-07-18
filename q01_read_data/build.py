# %load q01_read_data/build.py
import yaml
def read_data():
    with open( './data/ipl_match.yaml') as ipl:
        data = yaml.load(ipl)
        return data



