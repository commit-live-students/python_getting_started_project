#%load q04_count/build.py


def deliveries_count(data):
    
    import yaml

    data=open('./data/ipl_match.yaml','r')
    data1=yaml.load(data) 
    d=data1['innings'][0]['1st innings']['deliveries']

    #d1=d
    count=0
    
    for key,value in enumerate(d):
        value1=d[key]
    #print(value)
    #print(key,value,type(value))
        for k,v in value1.items():
            
            
        #print(v)
            if value1[k]['batsman']=='RT Ponting':
                
                count += 1

    return count


#deliveries_count(d1)












