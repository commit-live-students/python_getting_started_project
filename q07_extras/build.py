# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    l1=[]
    l2=[]
    # Write your code here
    b1=data['innings'][0]['1st innings']['deliveries']
    b2=data['innings'][1]['2nd innings']['deliveries']
    [[(l1.append(b1[i][j]['runs']['extras'])) for j in (b1[i].keys())] for i in range(0,len(b1))]
    [[(l2.append(b2[i][j]['runs']['extras'])) for j in (b2[i].keys())] for i in range(0,len(b2))]
    difference =sum(l2)-sum(l1)+4
    return difference
extras_runs(data)

