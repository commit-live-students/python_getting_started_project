import yaml

def read_data():
    f=open('./data/ipl_match.yaml')
    datadict=yaml.load(f)
    return datadict

def teams(datadict):
    team_list=datadict['info']['teams']
    return team_list
    


   
datadict=read_data()
teams(datadict)

