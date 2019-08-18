# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    bb_mac=[]
    dd1 = data['innings'][0]['1st innings']['deliveries']
    for delivery in dd1:
        for delivery_info in delivery.values():
            if delivery_info['batsman'] ==  "BB McCullum":
                bb_mac.append(delivery_info['runs']['batsman'])

    runs=sum(bb_mac)

    return(runs)
