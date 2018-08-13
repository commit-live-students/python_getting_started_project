# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
run = []


# Your Solution
def BC_runs(data):
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for deliver_key, deliver_val in delivery.items():
            if(deliver_val['batsman']=='BB McCullum'):
                run_scored = deliver_val['runs']['batsman']
                run.append (run_scored)
    runs = sum(run)
    return(runs)
