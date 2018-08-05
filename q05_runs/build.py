# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(runs):
    x1 = data['innings']
    x2 = x1[0]
    x3 = x2['1st innings']['deliveries']
    runs = 0
    for index, x in enumerate(x3):
        x4 = x3[index]
        for values in x4.values():
            x5 = x4.values()
            if values['batsman'] == 'BB McCullum':
                runs = runs + values['runs']['batsman']


    # Write your code here
    

    return(runs)


