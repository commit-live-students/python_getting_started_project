# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()



def BC_runs(data=data):
    runs=0
    deliveries=data['innings'][0]['1st innings']['deliveries']
    for k in deliveries:
        for i in k:
            if k[i]['batsman']=='BB McCullum':
                runs=k[i]['runs']['batsman']+runs
    return runs
BC_runs()
