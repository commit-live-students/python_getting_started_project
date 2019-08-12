import yaml

def read_data():

    path='./data/ipl_match.yaml'
    fo=open(path,'r')
    data=yaml.load(fo)
    # return data variable
    return data
#print read_data()
