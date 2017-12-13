# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    data1 = data['innings'][0]['1st innings']['deliveries'][:]
    for n in data1:
        batsman = n.values()[0]['batsman']
        if batsman == 'BB McCullum':
            runs = runs + n.values()[0]['runs']['batsman']

    return(runs)

print BC_runs(data)
print type(BC_runs(data))
