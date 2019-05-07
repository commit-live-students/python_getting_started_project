import yaml


def read_data():
    f=open('./data/ipl_match.yaml')
    datadict=yaml.load(f)
    return datadict

def deliveries_count(datadict):
    count=0
    deliveries=datadict['innings'][0]['1st innings']['deliveries']
    
    for delivery in deliveries:
        for key,value in delivery.items():
            batsman=value['batsman']
            if batsman=='RT Ponting':
                count+=1
    return count
            
datadict=read_data()
deliveries_count(datadict)
    
        
    
    

