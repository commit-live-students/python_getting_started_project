# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    innings1 = data['innings'][1]['2nd innings']['deliveries']
    extras1 = 0
    for n in innings1:
        if n.values()[0]['runs']['extras']!=0:
            extras1=extras1+n.values()[0]['runs']['extras']

    innings = data['innings'][0]['1st innings']['deliveries']
    extras = 0
    for m in innings:
        if m.values()[0]['runs']['extras']!=0:
            extras=extras+m.values()[0]['runs']['extras']
    difference =(extras1-extras)+4
    return difference
