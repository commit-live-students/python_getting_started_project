# %load q03_first_batsman/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(name):

    # Write your code here
    x = data['innings']
    y = x[0]
    z = y['1st innings']['deliveries']
    z1 = z[0]
    name = z1[0.1]['batsman']
    
    return name


