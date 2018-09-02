# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    delivery1 = data['innings'][0]['1st innings']['deliveries']
    extras1=[]
    for i in delivery1:
        for key in i:
            extras1.append(i[key]['runs']['extras'])
    delivery2 = data['innings'][1]['2nd innings']['deliveries']
    extras2=[]
    for j in delivery2:
        for key2 in j:
            extras2.append(j[key2]['runs']['extras'])
    difference=sum(extras2)-sum(extras1)+4
    return difference




