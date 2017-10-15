# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    global difference
    s1=0
    s2=0

    for x in data['innings'][0]['1st innings']['deliveries']:
        for k,v in x.items():
            if(v['runs']['extras']>0):
                s1+=1
    for x in data['innings'][1]['2nd innings']['deliveries']:
        for k,v in x.items():
            if(v['runs']['extras']>0):
                s2+=1

    # Write your code here
    s1
    s2
    difference =abs(s1-s2)


    return difference
d=extras_runs()
d
