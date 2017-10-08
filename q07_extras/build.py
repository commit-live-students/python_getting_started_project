# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    extras_first_innings=0
    extras_second_innings=0
    deliveries_first = data['innings'][0]['1st innings']['deliveries']
    deliveries_second = data['innings'][1]['2nd innings']['deliveries']

    for delivery in deliveries_first:
        for delivery_number, delivery_info in delivery.items():
                     if delivery_info['runs']['extras'] !=0:
                        extras_first_innings+=1


    for delivery in deliveries_second:
        for delivery_number, delivery_info in delivery.items():
                     if delivery_info['runs']['extras'] !=0:
                        extras_second_innings+=1
    difference =extras_second_innings-extras_first_innings


    return difference
