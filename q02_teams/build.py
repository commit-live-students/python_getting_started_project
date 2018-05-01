import yaml

def read_data():
 
    with open('./data/ipl_match.yaml', 'r') as stream:
        try:
            MyDict = yaml.load(stream)
            print(yaml.load(stream))
        except yaml.YAMLError as exc:
            print(exc)
    return MyDict




TeamDict = read_data()

def teams(TeamDict):
    teamList = TeamDict['info']['teams']
    return teamList



teams(TeamDict)



