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

def BC_runs(TeamDict):
    inningsInfo = TeamDict['innings'][0]
    deliveries_details = inningsInfo['1st innings']['deliveries']
    runs = 0
    for dictDetails in deliveries_details:    
        for x in dictDetails: 
            for val in dictDetails.values():
                    if((val['batsman']) == 'BB McCullum'):
                        runs += val['runs']['batsman']
                        
   
    return runs
BC_runs(TeamDict)

