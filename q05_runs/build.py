# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs  =0
    for i in data['innings'][0]['1st innings']['deliveries']:
        k=list(i.values())
        if(k[0]['batsman']=='BB McCullum'):
            runs = int(k[0]['runs']['batsman']) + runs


    return(runs)




