# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    deliveries=data['innings'][0]['1st innings']['deliveries']
    runs=0
    for balls in deliveries:
        if balls.values()[0]['batsman']=='BB McCullum':
            runs_scored=balls.values()[0]['runs']['batsman']
            runs=runs+runs_scored


    return(runs)
runs_scored=BC_runs(data)
print runs_scored
