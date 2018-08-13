# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    # Your code here
    for k,v in data['innings'][0].iteritems():
	       tmp = [i for i, x in enumerate(v['deliveries']) for e in x.values() if e['batsman'] == 'RT Ponting']
    count = len(tmp)
    return count
