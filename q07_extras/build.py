# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    e1= 0
    deliv1 = data['innings'][0]['1st innings']['deliveries']
    for d1 in deliv1:
        for d1_num, batsm1 in d1.items():
            if batsm1['runs']['extras']>0:
                e1+=1

    e2= 0
    deliv2 = data['innings'][1]['2nd innings']['deliveries']
    for d2 in deliv2:
        for d2_num, batsm2 in d2.items():
            if batsm2['runs']['extras']>0:
                e2+=1

    difference =e2-e1


    return difference



