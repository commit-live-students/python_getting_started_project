# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here

    runs1=0
    runs2=0
    deliveries1 = data['innings'][0]['1st innings']['deliveries']
    deliveries2 = data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries1:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['runs']['extras']>0:
                runs1=runs1+1
    for delivery in deliveries2:
        for delivery_number, delivery_info in delivery.items():
             if delivery_info['runs']['extras']>0:
                runs2=runs2+1

    difference =runs2-runs1


    return difference
