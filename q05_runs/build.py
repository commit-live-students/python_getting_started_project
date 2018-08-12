# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs=0
    name=data['innings'][0]['1st innings']['deliveries']
    for delivery in name:
        for delivery_number,delivery_info in delivery.items():
            if delivery_info['batsman']=='BB McCullum':
                run1=delivery_info['runs']
                runs+=run1['batsman']

    # Write your code here


    return(runs)

BC_runs(data)

