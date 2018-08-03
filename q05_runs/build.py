# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    delivery_list = data['innings'][0]['1st innings']['deliveries']
    runs = 0
    
    for delivery_detail in delivery_list:
        for delivery_detail_val in delivery_detail.values():
            for delivery_detail_values in delivery_detail_val:
                if(delivery_detail_values == 'batsman' and delivery_detail_val[delivery_detail_values] == 'BB McCullum'):
                    runs = runs + delivery_detail_val['runs']['batsman']

    return(runs)

BC_runs(data)

