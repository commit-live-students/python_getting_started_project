# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    run = 0
    deleiveries = data['innings'][0]['1st innings']['deliveries']
    for x in deleiveries:
        listd = list(x.values())
        if (listd[0]['batsman'] == 'BB McCullum'):
            run = run + int(listd[0]['runs']['batsman'])


    # Write your code here


    return(run)




