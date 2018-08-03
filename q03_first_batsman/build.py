# %load q03_first_batsman/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data):

    # Write your code here
    innings = data['innings']
    first_innings = innings[0]
    first_batsman = first_innings['1st innings']['deliveries'][0]
    return first_batsman[0.1]['batsman']

first_batsman(data)


