# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    # Write your code here
    first_inn = data['innings'][0]['1st innings']['deliveries']
    first_inn_extras = 0
    for k in first_inn:
        for key, value in k.iteritems():
            if value['runs']['extras'] > 0:
                first_inn_extras += 1
    
    
    second_inn = data['innings'][1]['2nd innings']['deliveries']
    second_inn_extras = 0
    for k in second_inn:
        for key, value in k.iteritems():
            if value['runs']['extras'] > 0:
                second_inn_extras += 1


    difference = second_inn_extras - first_inn_extras


    return difference
print extras_runs()


