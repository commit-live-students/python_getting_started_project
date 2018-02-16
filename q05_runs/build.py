# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs = 0
    innings = data['innings'][0]
    first_innings = innings['1st innings']
    deliveries = first_innings['deliveries']
    for k in deliveries:
        for key, value in  k.iteritems():
            if value['batsman'] == 'BB McCullum':
                runs = runs + value['runs']['batsman']
    return(runs)
print(BC_runs(data))
