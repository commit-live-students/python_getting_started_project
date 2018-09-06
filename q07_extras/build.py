#%load q07_extras/build.py

import yaml

def extras_runs(data):
 
    data=open('./data/ipl_match.yaml','r')
    data1=yaml.load(data)
    data_2nd=data1['innings'][1]['2nd innings']['deliveries']

    data_1st=data1['innings'][0]['1st innings']['deliveries']
    count1=[]
    count2=[]
    for key,value in enumerate(data_2nd):
       
        for k,v in value.items():
            
            if v['runs']['extras']>0:
                
                count2.append(v['runs']['extras'])
            
        
   

    for key1,value1 in enumerate(data_1st):
       
        for k1,v1 in value1.items():
            if v1['runs']['extras']>0:
                count1.append(v1['runs']['extras'])

#print(len(count1))        
    difference=(len(count2)-len(count1))  
    
    return difference







