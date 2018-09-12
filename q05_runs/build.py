# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs=0
    list_deliveries= data['innings'][0]['1st innings']['deliveries']
    count=0
    for delivery in list_deliveries:
        for delivery_number,delivery_info in delivery.items():
            if delivery_info['batsman']== 'BB McCullum':
                count+=1
                runs+=delivery_info['runs']['batsman']
    print('Runs scored by BC Cullum is: %i' %runs)
    return(runs)

BC_runs(data)


