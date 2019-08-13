import yaml

def read_data():
    path = './data/ipl_match.yaml'
    docs11 = open(path,'r')
    docs1 = yaml.load(docs11)
    return docs1
