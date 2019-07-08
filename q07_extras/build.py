# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    extras1=0
    a=data['innings'][0]['1st innings']['deliveries']
    # Write your code here
    for i in range(len(a)):
        for j in a[i].values():
            for k in j['runs']:
                extras1=extras1+(j['runs']['extras'])
    
    extras2=0
    b=data['innings'][1]['2nd innings']['deliveries']
    for i in range(len(b)):
        for j in b[i].values():
            for k in j['runs']:
                extras2=extras2+(j['runs']['extras'])
    return abs((extras2)-(extras1))
    

c=extras_runs(data)
c


