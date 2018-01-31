# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    # Write your code here
    runs=0
    d= data['innings'][0]['1st innings']['deliveries']
    l= len(d)
    for i in range(0, l):
        k=d[i].keys()
        if d[i][k[0]]['batsman']=='BB McCullum':
            runs+=d[i][k[0]]['runs']['batsman']
    return(runs)
