# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    d1 = data['innings'][0]['1st innings']['deliveries']
    inning1_extras=0
    for i in d1:
        for delivery_no ,delivery_info in i.items():
            if (delivery_info['runs']['extras'] >= 1):
                inning1_extras = inning1_extras + 1

    d2 = data['innings'][1]['2nd innings']['deliveries']
    inning2_extras=0
    for i in d2:
           for delivery_no ,delivery_info in i.items():
                 if (delivery_info['runs']['extras'] >= 1):
                    inning2_extras = inning2_extras + 1

    difference = inning2_extras - inning1_extras
    return difference
