# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    global runs
    runs=0

    for x in data['innings'][0]['1st innings']['deliveries']:
        x
        for k,v in x.items():
            k
            if(v['batsman']=='BB McCullum'):
                runs+=v['runs']['batsman']

    return(runs)
BC_runs(data)
