import yaml

def read_data():
    f=open('./data/ipl_match.yaml')
    datadict=yaml.load(f)
    return datadict

def extras_runs(datadict):
    deliveries=datadict['innings'][0]['1st innings']['deliveries']
    extras_1=0
    for delivery in deliveries:
        for key,value in delivery.items():
            
            if value['runs']['extras'] >0:
                extras_1+=1     
            
    deliveries=datadict['innings'][1]['2nd innings']['deliveries']
    extras_2=0
    for delivery in deliveries:
        for key,value in delivery.items():
            if value['runs']['extras'] >0:
                extras_2+=1
            
    difference=extras_2-extras_1
    return(difference)
datadict=read_data()
extras_runs(datadict)

