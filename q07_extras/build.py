# Default Imports
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    dely = data['innings'][0]['1st innings']['deliveries']
    loop_var = 0
    extras_in_1st = 0
    for batsman in dely:
        ind = data['innings'][0]['1st innings']['deliveries'][loop_var].keys()
        extra_or_not = data['innings'][0]['1st innings']['deliveries'][loop_var][ind[0]].keys()
        if extra_or_not[len(extra_or_not) - 2] == 'extras':
            extras_in_1st = extras_in_1st + 1
        loop_var = loop_var + 1


    dely = data['innings'][1]['2nd innings']['deliveries']
    loop_var = 0
    extras_in_2nd = 0
    for batsman in dely:
        ind = data['innings'][1]['2nd innings']['deliveries'][loop_var].keys()
        extra_or_not = data['innings'][1]['2nd innings']['deliveries'][loop_var][ind[0]].keys()
        if extra_or_not[len(extra_or_not) - 2] == 'extras':
            extras_in_2nd = extras_in_2nd + 1
        loop_var = loop_var + 1
    difference = extras_in_2nd - extras_in_1st

    return difference

print extras_runs(data)
