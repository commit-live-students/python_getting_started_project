# %load q03_first_batsman/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):
    a = data['innings'][0]
    b = a['1st innings']['deliveries'][0]
    name = b[0.1]['batsman']

    




    return name



