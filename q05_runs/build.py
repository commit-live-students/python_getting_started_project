# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data=data):
    runs = 0
    for delivery in data['innings'][0]['1st innings']['deliveries']:
        keys = delivery.keys()
        for key in keys:
            if(delivery[key]['batsman'] == 'BB McCullum'):
                runs +=delivery[key]['runs']['batsman']                       

    return(runs)

BC_runs()






