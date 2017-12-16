# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    count=data['innings'][0]['1st innings']['deliveries']
    no_of_runs=0
    for n in count:
        if n.values()[0]['batsman']=='BB McCullum':
            no_of_runs=no_of_runs+n.values()[0]['runs'].values()[0]
    return(no_of_runs)
