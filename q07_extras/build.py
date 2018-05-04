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
def extras_runs(TeamDict):
    extraInnings1 = []  
    extraInnings2 = []
    difference = 0
    no_of_byes = 4
    inningsInfo1 = TeamDict['innings'][0]
    deliveries_details1 = inningsInfo1['1st innings']['deliveries']
    diffcount = 0
    for dictDetails1 in deliveries_details1:    
        for x in dictDetails1: 
            for val1 in dictDetails1.values():               
                    extraInnings1.append((val1['runs']['extras']))
                         
    inningsInfo2 = TeamDict['innings'][1]
    deliveries_details2 = inningsInfo2['2nd innings']['deliveries']
    
    for dictDetails2 in deliveries_details2:    
        for x in dictDetails2: 
            for val2 in dictDetails2.values():              
                    extraInnings2.append((val2['runs']['extras']))

    s0 = sum(extraInnings1)
    s1 = s0 - no_of_byes
    s2 = sum(extraInnings2)
    difference = s2-s1
    return difference
extras_runs(TeamDict)


