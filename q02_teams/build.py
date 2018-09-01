#%load q02_teams/build.py

import yaml

def teams(data):
    data1=open('./data/ipl_match.yaml','r')
    data=yaml.load(data1)
    
    teams1=data['info']['teams']
    
    return teams1
    


 

        
       
        
    
    

    
    
    
    
    
    
    





