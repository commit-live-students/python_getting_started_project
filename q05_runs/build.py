# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(*data):
    runs = 0
    for n in data:
        runs += n 

    # Write your code here


    return(runs)
