# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    
    delivery1=data['innings'][0]['1st innings']['deliveries']
    extra_array1=[]
    for index in range(len(delivery1)):
        for key in delivery1[index]:
            if(delivery1[index][key]['runs']['extras']>0):
                extra_array1.append(delivery1[index][key]['runs']['extras'])
        
    extras1=len(extra_array1)

    delivery2=data['innings'][1]['2nd innings']['deliveries']
    extra_array2=[]
    for index in range(len(delivery2)):
        for key in delivery2[index]:
            if(delivery2[index][key]['runs']['extras']>0):
                extra_array2.append(delivery2[index][key]['runs']['extras'])
        
    extras2=len(extra_array2)
    difference = extras2-extras1
    return difference
extras_runs(data)


