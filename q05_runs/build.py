# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['batsman'] == 'BB McCullum':
                runs+= delivery_info['runs']['batsman']
                


    return(runs)

BM=BC_runs(data)
print(BM)

# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
deliveries = data['innings'][0]['1st innings']['deliveries'][0][0.1]['runs']
deliveries
deliveries = data['innings'][0]['1st innings']['deliveries']
deliveries


