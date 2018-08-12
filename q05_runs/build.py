# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    for a in data['innings'][0]['1st innings']['deliveries']:
        for key in a:
            if a[key]['batsman'] == "BB McCullum":
                runs += a[key]['runs']['batsman']

    return(runs)
