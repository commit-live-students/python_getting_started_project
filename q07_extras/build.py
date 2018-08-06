# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data):

    # Write your code here
    x1 = data['innings']
    x2 = x1[0]
    x3 = x2['1st innings']['deliveries']
    extras1 = 0
    for index, x in enumerate(x3):
        x4 = x3[index]
        for values in x4.values():
            #x5 = x4.values()
            if values['runs']['extras'] != 0:
                extras1 = extras1 + 1

    x22 = x1[1]
    x33 = x22['2nd innings']['deliveries']
    extras2 = 0
    for index, x in enumerate(x33):
        x44 = x33[index]
        for values in x44.values():
            #x55 = x44.values()
            if values['runs']['extras'] != 0:
                extras2 = extras2 + 1

    difference = abs(extras1 - extras2)

    return difference


