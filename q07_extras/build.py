# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here

    deliveries1 = data['innings'][0]['1st innings']['deliveries']
    deliveries2 = data['innings'][1]['2nd innings']['deliveries']

    difference = abs(
        len([ v['runs']['extras'] for d in deliveries1 for k,v in d.items() if v['runs']['extras']>0 ])
            -len([ v['runs']['extras'] for d in deliveries2 for k,v in d.items() if v['runs']['extras']>0]))
    return difference
