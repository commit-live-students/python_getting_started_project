# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    deliveries = data['innings'][0]['1st innings']['deliveries']
    #deliveries
    runs =0
    for i1 in deliveries:
        #print(i)
        for i2 in i1.items():
            if i2[1]['batsman'] == 'BB McCullum':
                runs = runs+i2[1]['runs']['batsman']
            #print(i2)
        # Write your code here
    return(runs)

deliveries = data['innings'][0]['1st innings']['deliveries']
#deliveries
c =0
for i1 in deliveries:
    #print(i)
    for i2 in i1.items():
        if i2[1]['batsman'] == 'BB McCullum':
            c = c+i2[1]['runs']['batsman']
        #print(i2)


