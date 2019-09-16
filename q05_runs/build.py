# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def BC_runs(data):
    runs = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for i in deliveries:
        for j in i:
            if i[j]['batsman'] == 'BB McCullum':
                runs += i[j]['runs']['batsman']
    return(runs)

BC_runs(data)
a = data['innings'][0]['1st innings']['deliveries'][:10]
# print a
#print a[0][0.1]['runs']['batsman']
'''
runs = 0
for i in a:
    for j in i:
        if a[j]['batsman'] == 'BB McCullum':
            runs += a[i][j]['runs']['batsman']
print runs
'''
print a
runs = 0
for i in a:
    for j in i:
        if i[j]['batsman'] == 'BB McCullum':
            runs += i[j]['runs']['batsman']
        #print i[j]['batsman'], i[j]['runs']['batsman']
            
print runs

