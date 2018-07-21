# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    extrasinnnings_1=[]
    extrasinnnings_2=[]
    deliveries=data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for key in delivery:
            extrasinnnings_1.append(delivery[key]['runs']['extras'])
    deliveries=data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries:
        for key in delivery:
            extrasinnnings_2.append(delivery[key]['runs']['extras'])
    count1=0
    count2=0
    for extra in extrasinnnings_1:
        if extra>0:
            count1+=1
    for extra in extrasinnnings_2:
        if extra>0:
            count2+=1
    difference=count2-count1
    return difference


