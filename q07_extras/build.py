# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    extra2 =[]
    for i in data['innings'][1]['2nd innings']['deliveries']:
        k=list(i.values())
        if ('extras' in k[0] ):
            extra2.append(list(k[0]['extras'].values())[0])
    extra1 =[]
    for i in data['innings'][0]['1st innings']['deliveries']:
        k=list(i.values())
        if ('extras' in k[0] ):
            extra1.append(list(k[0]['extras'].values())[0])
        

    # Write your code here


    difference = len(extra2) - len(extra1)


    return difference








