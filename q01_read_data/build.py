# %load q01_read_data/build.py

import yaml

def read_data():
    with open('./data/ipl_match.yaml', 'r') as x:
        data=yaml.load(x)  
    return (data)


print(read_data())



