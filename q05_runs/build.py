import yaml

def read_data():
    f=open('./data/ipl_match.yaml')
    datadict=yaml.load(f)
    return datadict

def BC_runs(datadict):
    deliveries=datadict['innings'][0]['1st innings']['deliveries']
    runs=0
    for delivery in deliveries:
        for key,value in delivery.items():
            batsman=value['batsman']
            if batsman=='BB McCullum':
                runs+=value['runs']['batsman']
    return runs
datadict=read_data()
BC_runs(datadict)
        

