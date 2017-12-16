# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    deliv1=data['innings'][0]['1st innings']['deliveries']
    deliv2=data['innings'][1]['2nd innings']['deliveries']
    # Write your code here
    d1=list()
    count = 0
    for i in range(len(deliv1)):
        d1.append(deliv1[i].items()[0][0])
    d2=list()
    count = 0
    for i in range(len(deliv2)):
        d2.append(deliv2[i].items()[0][0])

    extras_d1 = 0
    extras_d2 = 0

    for i in range(len(deliv1)):
        temp = d1[i]
        if(deliv1[i][temp]['runs']['extras']!=0):
            extras_d1 +=1
    for i in range(len(deliv2)):
        temp = d2[i]
        if(deliv2[i][temp]['runs']['extras']!=0):
            extras_d2 +=1

    difference = extras_d2 - extras_d1

    return difference
