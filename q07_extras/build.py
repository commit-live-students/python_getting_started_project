# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
def extras_runs(data=data):
    find1=data['innings'][0]['1st innings']['deliveries']
    find2=data['innings'][1]['2nd innings']['deliveries']
    extras1=[]
    extras2=[]
    for i in find1:
        if i.values()[0]['runs']['extras']!=0:
            extras1.append(i.values()[0]['runs']['extras'])
    for i in find2:
        if i.values()[0]['runs']['extras']!=0:
            extras2.append(i.values()[0]['runs']['extras'])
    difference = len(extras2)-len(extras1)
    return difference
