# %load q03_first_batsman/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):
    info = data['info']
    deliveries = data['innings'][0]['1st innings']['deliveries']
    bastman = deliveries[0][0.1]['batsman']
    return bastman

print(first_batsman(data))




