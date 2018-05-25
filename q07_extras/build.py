# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    extra1=extra2=0
    lst1 = data['innings'][0]['1st innings']['deliveries']
    for value in lst1:
        for k2,v2 in value.items():
            if v2['runs']['extras']!=0:
                extra1+=1
    lst2 = data['innings'][1]['2nd innings']['deliveries']
    for value in lst2:
        for k2,v2 in value.items():
            if v2['runs']['extras']!=0:
                extra2+=1
    difference =abs(extra1-extra2)
    return difference


