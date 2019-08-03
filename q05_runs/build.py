# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def BC_runs(data):

    # Your code here
    dely = data['innings'][0]['1st innings']['deliveries']
    loop_var = 0
    runs = 0
    for batsman in dely:
        ind = data['innings'][0]['1st innings']['deliveries'][loop_var].keys()
        batsman = data['innings'][0]['1st innings']['deliveries'][loop_var][ind[0]]['batsman']

        if batsman == 'BB McCullum':
            ind_runs = data['innings'][0]['1st innings']['deliveries'][loop_var][ind[0]]['runs']['batsman']
            runs=runs + ind_runs
        loop_var=loop_var + 1
    return(runs)

print BC_runs(data)
