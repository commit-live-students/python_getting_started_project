# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    extras1, extras2 = 0, 0
    deliveries1 = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries1:
        for del_info in delivery.values():
             if del_info['runs']['extras'] != 0:
                    extras1 += 1
    deliveries2 = data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries2:
        for del_info in delivery.values():
             if del_info['runs']['extras'] != 0:
                    extras2 += 1

    difference = extras2 - extras1
    return difference
