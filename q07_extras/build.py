from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def extras_runs(data=data):
    
    e1=[]
    d1=data['innings'][0]['1st innings']['deliveries']    
    for index,v in enumerate(d1):
        for key,va in v.items():
            for key,val in va.items():
                if key=='extras':
                    for key,values in val.items():
                        e1.append(values)
    
    e2=[]
    d2=data['innings'][1]['2nd innings']['deliveries']
    for index,v in enumerate(d2):
        for key,va in v.items():
            for key,val in va.items():
                if key=='extras':
                    for key,values in val.items():
                        e2.append(values)
                            
    difference=len(e2)-len(e1)
    
    return difference

