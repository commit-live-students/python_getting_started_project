from greyatomlib.python_getting_started.q01_read_data.build import read_data
import pprint
data = read_data()

def extras_runs(data=data):
    deliveries= data['innings'][0]['1st innings']['deliveries']
    deliveries_2 = data['innings'][1]['2nd innings']['deliveries']
    extras_1 = 0
    extras_2 = 0

    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if (delivery_info['runs']['extras']>=1):
                extras_1 = extras_1+ 1

    for delivery in deliveries_2:
        for delivery_number, delivery_info in delivery.items():
             if (delivery_info['runs']['extras']>=1):
                    extras_2 = extras_2+ 1

    difference =extras_2 - extras_1
    return difference
