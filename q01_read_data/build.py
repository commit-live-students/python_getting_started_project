import yaml

def read_data():
    data1 = open('./data/ipl_match.yaml','r')
    data = yaml.load(data1)
    return data;

print read_data();
