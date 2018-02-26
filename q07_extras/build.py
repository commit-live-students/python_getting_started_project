# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    extras1=[]
    extras2=[]

    d= data['innings'][0]['1st innings']['deliveries']
    l= len(d)
    for i in range(0, l):
        k=d[i].keys()
        if d[i][k[0]]['runs']['extras']!=0:
            extras1.append(d[i][k[0]]['runs']['extras'])

    # Write your code here
    d2= data['innings'][1]['2nd innings']['deliveries']
    l2= len(d2)
    for i in range(0, l2):
        k2=d2[i].keys()
        if d2[i][k2[0]]['runs']['extras']!=0:
            extras2.append(d2[i][k2[0]]['runs']['extras'])


    difference = abs(len(extras1) - len(extras2))


    return difference
