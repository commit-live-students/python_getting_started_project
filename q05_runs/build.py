from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def BC_runs(data=data):
    runs=0
    d=data['innings'][0]['1st innings']['deliveries']
    for i in d:
        for v in i.values():
            for key,values in v.items():
                if key=='batsman':
                    if values=='BB McCullum':
                        runs=v.get('runs')['batsman']+runs
                            
    return runs                   
    


