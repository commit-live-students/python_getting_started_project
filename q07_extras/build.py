# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    # Write your code here
    first_extra = []
    for k,v in data['innings'][0].iteritems():
        first_extra = [e['runs']['extras'] for i, x in enumerate(v['deliveries']) for e in x.values() if e['runs']['extras'] > 0]

    secnd_extra = []
    for k,v in data['innings'][1].iteritems():
        secnd_extra = [e['runs']['extras'] for i, x in enumerate(v['deliveries']) for e in x.values() if e['runs']['extras'] > 0]

    difference = len(secnd_extra) - len(first_extra)
    return difference
