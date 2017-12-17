# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs=0
    batsman = data['innings'][0]['1st innings']['deliveries']
    for rp in batsman:
    #print rp.values()[0]['runs']['batsman']
        if rp.values()[0]['batsman'] == 'BB McCullum':
            runs = runs + rp.values()[0]['runs']['batsman']
    return(runs)
#print BC_runs(data)
