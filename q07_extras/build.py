# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def extras_runs(data=data):
    # Write your code here
    first_inn_extras = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for lst in deliveries:
        for overs in lst:
            if lst[overs]["runs"]["extras"]!=0:
                first_inn_extras = first_inn_extras + 1 #list[overs]['runs']['extras']

# Your Solution
    second_inn_extras = 0
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for lst in deliveries:
        for overs in lst:
            if lst[overs]["runs"]["extras"]!=0:
                second_inn_extras = second_inn_extras + 1 #list[overs]['runs']['extras']

    #print second_inn_extras
    difference = second_inn_extras - first_inn_extras
    #print difference
    return difference
