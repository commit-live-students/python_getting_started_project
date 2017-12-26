# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
runs=0

# Your Solution
def BC_runs(data):
    deliveries=data['innings'][0]['1st innings']['deliveries']
    global runs
    for item in deliveries:
        for key,values in item.items():
            if values['batsman']=='BB McCullum':
                runs =runs+values['runs']['batsman']
    return(runs)
