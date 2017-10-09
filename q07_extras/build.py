# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    d1 = data['innings'][0]['1st innings']['deliveries']
    inning1_extras=0
    for i in d1:
        for delivery_no ,delivery_info in i.items():
            inning1_extras = inning1_extras + delivery_info['runs']['extras']




    d2 = data['innings'][1]['2nd innings']['deliveries']
    inning2_extras=0
    for i in d2:
        for delivery_no ,delivery_info in i.items():
            inning2_extras = inning2_extras + delivery_info['runs']['extras']



    difference = inning2_extras - inning1_extras




    


    return difference
