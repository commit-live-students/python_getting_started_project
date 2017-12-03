# %load q03_first_batsman/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):
    f = {}
    g = {}
    h = {}
    i = {}
    f = data['innings'][0]
    g = f['1st innings']
    h = g['deliveries'][0]
    i = h.values()
    j = i[0]
    name = j['batsman']
    return name
