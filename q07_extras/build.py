# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    data1= data['innings'][0]['1st innings']['deliveries']
    extras1=[]
    for i in data1:
        if i.values()[0].get('runs')!=None:
            if i.values()[0]['runs']['extras']!=0:
                extras1.append(i.values()[0]['runs']['extras'])
    data2= data['innings'][1]['2nd innings']['deliveries']
    extras2=[]
    for i in data2:
        if i.values()[0].get('runs')!=None:
            if i.values()[0]['runs']['extras']!=0:
                extras2.append(i.values()[0]['runs']['extras'])
    difference = len(extras2)-len(extras1)
    return difference
