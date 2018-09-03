# %load q01_read_data/build.py
import yaml
import os

def read_data():
    filepath='/data/ipl_match.yaml'
    path=os.getcwd()+filepath
    with open(path,'r') as data:
        data=yaml.load(data)
    return data

