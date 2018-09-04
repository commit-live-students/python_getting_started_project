# %load q03_first_batsman/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
    # Write your code here
def first_batsman(data=data):
    x=data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
    return x

first_batsman()
   # return name




