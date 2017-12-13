import yaml

def read_data():

    path = './data/ipl_match.yaml'

    data= open(path, 'r')
    d1 = yaml.load(data)
    return d1
