#%load q06_bowled_players/build.py

import yaml

def bowled_out(data):
    data=open('./data/ipl_match.yaml','r')
    data1=yaml.load(data)
    data2=data1['innings'][1]['2nd innings']['deliveries']
    bowled_players=[] 
    for key,value in enumerate(data2):
        for k,v in value.items():
            if 'wicket' in v.keys():
                if (v['wicket']['kind'])=='bowled':
                    bowled_players.append(v['wicket']['player_out'])
#print(bowled_players)
                #
            
            
    return (bowled_players)        
            #print(v.keys())
        #if v.keys() =='wicket':#['wicket']['kind']=='bowled':
            #print(v)
        
            #print(v)
        
    #print(type(value))
#print(data2)



