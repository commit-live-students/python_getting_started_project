import yaml
def read_data():
    path='./data/ipl_match.yaml'
    data1=open(path,'r')
    data=yaml.load(data1)
    return data
