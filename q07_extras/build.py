# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    for x,y in zip(inning,extras):
        if x=='1' and len(y)!=0:
            ext1.append(int(y))
        elif x=='2' and len(y)!=0:
            ext2.append(int(y))
    # Write your code here
    difference = ext1-ext2

    return difference




