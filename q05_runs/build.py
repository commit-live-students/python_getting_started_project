# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs=0
    deliveries=data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for delivery_no,delivery_info in delivery.items():
            if(delivery_info['batsman']=='BB McCullum'):
                runs=runs+delivery_info['runs']['batsman']
    return(runs)
