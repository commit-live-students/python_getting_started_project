# %load q01_read_data/build.py
import yaml
import os
def read_data():
    data ={}
    data = yaml.load(open('./data/ipl_match.yaml','r'))
    # return data variable
    return data

read_data()




