# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    ex1=0
    ex2=0
    total_del_1st_innings=len(data['innings'][0]['1st innings']['deliveries'])
    total_del_2nd_innings=len(data['innings'][1]['2nd innings']['deliveries'])
    lst1=data['innings'][0]['1st innings']['deliveries']
    lst2=data['innings'][1]['2nd innings']['deliveries']
    for i in range(total_del_1st_innings):
        for x,y in lst1[i].items():
            if lst1[i][x]['runs']['extras']>0:
                ex1+=1
    for i in range(total_del_2nd_innings):
        for x,y in lst2[i].items():
            if lst2[i][x]['runs']['extras']>0:
                ex2+=1
            
    
    difference=ex2-ex1


    return difference
extras_runs()

