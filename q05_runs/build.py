from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def BC_runs(data=data):
    runs =0 
    deliveries = data['innings'][0]['1st innings']['deliveries']
    b=0.1
    for a in range(len(deliveries)):
        for b in deliveries[a]:
            runs_all = deliveries[a][b]['runs']['batsman']
            if(deliveries[a][b]['batsman']=='BB McCullum'):
                runs = runs+runs_all
               
    return runs
BC_runs()

