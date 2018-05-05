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
def bowled_out(TeamDict):
    inningsInfo = TeamDict['innings'][1]
    deliveries_details = inningsInfo['2nd innings']['deliveries']
    bowled_out_players = []
    for dictDetails in deliveries_details:    
        for x in dictDetails: 
            for val in dictDetails.values():
                if('wicket' in val.keys()):
                    if(val['wicket']['kind']) == 'bowled':
                        bowled_out_players.append(val['wicket']['player_out'])
    
    return bowled_out_players
bowled_out(TeamDict)

