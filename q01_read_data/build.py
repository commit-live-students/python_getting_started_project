import yaml

def read_data():
    
    d= open('./data/ipl_match.yaml','r')
    data = yaml.load(d)
    return data

read_data()

