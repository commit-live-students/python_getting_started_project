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

def first_batsman(TeamDict):
    inningsInfo = TeamDict['innings'][0]
    fbatsman = inningsInfo['1st innings']['deliveries'][0][0.1]['batsman']
    return fbatsman
first_batsman(TeamDict)


