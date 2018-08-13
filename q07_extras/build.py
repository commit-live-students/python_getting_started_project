# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):



    # Write your code here
    extras1st=0
    extras2nd=0
    extras=data['innings'][0]['1st innings']['deliveries']
    extras2=data['innings'][1]['2nd innings']['deliveries']
    for x in  extras:
        for y in x:
               if  x[y]['runs']['extras']!=0:
                     extras1st=extras1st + 1
    for w in  extras2:
        for z in w :
                if w[z]['runs']['extras']!=0:
                    extras2nd=extras2nd+ 1



    difference =int(extras2nd) - int(extras1st)


    return difference
