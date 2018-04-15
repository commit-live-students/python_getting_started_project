import yaml
def read_data():
    f=open('./data/ipl_match.yaml')
    theDict = yaml.load(f)
    
    return theDict
read_data()

