# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    innings = data['innings']
    first_innings = innings[0]
    deliveries = first_innings['1st innings']['deliveries']
    for item in deliveries:
        for k, v in item.items():
            if(v['batsman'] == 'BB McCullum'):
                runs = runs + v['runs']['batsman']

	    
    return runs

BC_runs(data)



