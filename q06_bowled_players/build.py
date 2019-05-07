import yaml

def read_data():
    f=open('./data/ipl_match.yaml')
    datadict=yaml.load(f)
    return datadict

def bowled_out(datadict):
    bowled_players=[]
    deliveries=datadict['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries:
        for key, value in delivery.items():
            if 'wicket' in value.keys():
                if value['wicket']['kind']=='bowled':
                    bowled_players.append(value['wicket']['player_out'])
    return bowled_players
    
datadict=read_data()
bowled_out(datadict)





