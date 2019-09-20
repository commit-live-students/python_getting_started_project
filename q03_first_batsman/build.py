# %load q03_first_batsman/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def first_batsman(data = data):
    innings = data['innings'][0]
    first_innings = innings['1st innings']
    deliveries = first_innings['deliveries']
    first_ball =(deliveries[0] [0.1])
    first_batsman = first_ball['batsman']
    return(first_batsman)
print(first_batsman(data))
