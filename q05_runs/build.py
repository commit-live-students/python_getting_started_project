# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    run = 0
    deleiveries = data['innings'][0]['1st innings']['deliveries']
    for x in deleiveries:
        listtest = list(x.values())
        if (listtest[0]['batsman'] == 'BB McCullum'):
            run = run + int(listtest[0]['runs']['batsman'])


    return(run)


BC_runs(data)


