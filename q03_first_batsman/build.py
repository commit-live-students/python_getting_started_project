# %load q03_first_batsman/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):

    # Write your code here


    temp_1 = data.get('innings', {})
    temp_2 = temp_1[0]['1st innings']['deliveries'][0]
    name = temp_2.get(0.1,{}).get('batsman')

    return name

first_batsman()


