# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    list1 = []
    list2 = []

    # Write your code here
    dat1 = data['innings'][0]['1st innings']['deliveries']
    dat2 = data['innings'][1]['2nd innings']['deliveries']
    # Write your code here
    for i in list(range(len(dat1))):
        for key in dat1[i]:
            list1.append(dat1[i][key]['runs']['extras'])
            

    # Write your code here
    for i in list(range(len(dat2))):
        for key in dat2[i]:
            list2.append(dat2[i][key]['runs']['extras'])

    difference = sum(list2) - sum(list1)


    return difference





