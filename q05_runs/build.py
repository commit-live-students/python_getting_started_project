# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data = data):
    runs = 0
    subset_of_data = data['innings'][0]['1st innings']['deliveries']
    for i in subset_of_data:        
        if i.values()[0]['batsman'] == 'BB McCullum':
            runs = runs + i.values()[0]['runs'].values()[0]
    return(runs)

BC_runs()
