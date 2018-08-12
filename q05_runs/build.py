# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
from pprint import pprint

# Your Solution
def BC_runs(data):

    deliveries=data['innings'][0]['1st innings']['deliveries']
    current_delivery=0
    runs=0
    #print(deliveries)
    for delivery in deliveries:

        #current_delivery+=0.1
        #print(delivery)
        (k, v), = delivery.items()
        current_batsman=v['batsman']
        #print(v['batsman'])
        if current_batsman=='BB McCullum':
            runs+=v['runs']['batsman']
            #count+=1
            #print(count)




    return(runs)

#pprint(data)
