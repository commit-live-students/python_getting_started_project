# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    for k,v in data['innings'][0].iteritems():
	       tmp = [e['runs']['batsman'] for i, x in enumerate(v['deliveries']) for e in x.values() if e['batsman'] == 'BB McCullum']
    runs = sum(tmp)
    return(runs)
