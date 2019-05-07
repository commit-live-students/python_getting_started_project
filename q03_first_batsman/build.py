import yaml

def read_data():
    f=open('./data/ipl_match.yaml')
    datadict=yaml.load(f)
    return datadict

def first_batsman(datadict):
    name=datadict['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
    return name
    
datadict=read_data()
first_batsman(datadict)


