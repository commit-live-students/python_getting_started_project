# %load q03_first_batsman/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):
    name =  batsman_name = data['innings'][0].get('1st innings').get('deliveries')[0].get(0.1).get('batsman')
    return name


















