# %load q03_first_batsman/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):

    first_inning_data = data['innings'][0]['1st innings']
    first_ball_data = first_inning_data['deliveries'][0]
    name = first_ball_data[0.1]['batsman']
    
    return name

first_batsman(data)


