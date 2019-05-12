# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
list1=[]
list2=[]
# Your Solution
def extras_runs(data=data):

    # Write your code here
    data1=data['innings'][0]['1st innings']['deliveries']
    for i in data1:
        data2=list(i.values())
        if (data2[0]['runs']['extras'])>0:
            list1.append(data2[0]['runs']['extras'])
        
    data3=data['innings'][1]['2nd innings']['deliveries']
    for i in data3:
        data4=list(i.values())
        if (data4[0]['runs']['extras'])>0:
            list2.append(data4[0]['runs']['extras'])
       
    difference =len(list2)-len(list1)


    return difference


