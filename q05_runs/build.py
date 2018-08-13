# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    d = data['innings'][0]['1st innings']['deliveries']
    my_list = [a[k] for a in d for k in a if a[k]['batsman'] == 'BB McCullum']
    runs = sum([x['runs']['batsman'] for x in my_list])
    return(runs)
