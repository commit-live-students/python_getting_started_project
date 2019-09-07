# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    total = data['innings'][0]['1st innings']['deliveries']

    for b in total:
        for k in b:
            if b[k]['batsman'] == 'BB McCullum' and b[k]['runs']['batsman'] != 0:

                runs += b[k]['runs']['batsman']

    return(runs)
