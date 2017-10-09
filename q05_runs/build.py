# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    deliveries = data['innings'][0]['1st innings']['deliveries']
    runs = 0
    for i in deliveries:
        for delivery_number, delivery_info in i.items():
            if delivery_info['batsman']=="BB McCullum":
                runs = runs + delivery_info['runs']['batsman']


    return(runs)
