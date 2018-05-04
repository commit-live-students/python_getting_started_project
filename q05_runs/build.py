
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def BC_runs(data=data):
    runs=0
    deli = (data['innings'][0]['1st innings']['deliveries'])
    deli_len = len(deli)
    
    for ctr in range(deli_len):
        no_balls=(list(deli[ctr]))
        balls=float(no_balls[0])
        
        if deli[ctr][balls]['batsman'] == 'BB McCullum':
            runs+= int(deli[ctr][balls]['runs']['batsman'])

    return(runs)
print(BC_runs())


