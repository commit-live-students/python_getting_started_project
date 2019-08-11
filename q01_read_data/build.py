import yaml

def read_data():

    file='./data/ipl_match.yaml'
    fo=open(file,'r')
    data=yaml.load(fo)
    return data
