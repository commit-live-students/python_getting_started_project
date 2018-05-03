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
nos_of_delivery = len(TeamDict['innings'][0]['1st innings']['deliveries'])
print(nos_of_delivery)



def deliveries_count(TeamDict):
    inningsInfo = TeamDict['innings'][0]
    deliveries_details = inningsInfo['1st innings']['deliveries']
    count = 0
    for dictDetails in deliveries_details:    
        for x in dictDetails: 
            for val in dictDetails.values():
                    if((val['batsman']) == 'RT Ponting'):
                        count += 1
   
    return count
deliveries_count(TeamDict)

