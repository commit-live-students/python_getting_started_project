# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    ext1 = 0
    ext2 = 0
    dt1 = data['innings'][0]['1st innings']['deliveries']
    dt2 = data['innings'][1]['2nd innings']['deliveries']

    for i in range(len(dt1)):
        x = dt1[i].keys()
        if(dt1[i][x[0]]["runs"]["extras"]==1):
            ext1 = ext1 + 1
    for i in range(len(dt2)):
        x = dt2[i].keys()
        if(dt2[i][x[0]]["runs"]["extras"]==1):
            ext2 = ext2 + 1
    difference = ext2 - ext1 -1
    return difference
