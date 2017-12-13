import yaml

def read_data():
    path= './data/ipl_match.yaml'
    data = open(path,'r')
    data1= yaml.load(data)
    return data1
