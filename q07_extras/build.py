# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    difference=0
    innings1= data['innings'][1]['2nd innings']['deliveries']
    innings= data['innings'][0]['1st innings']['deliveries']
    extras1 = 1
    extras = 1

    for n in innings1:
        if n.values()[0]['runs']['extras']!=0:
            extras1=extras1+1



    for n in innings:
        if n.values()[0]['runs']['extras']!=0:
            extras=extras+1
            difference=extras1-extras
    return difference
