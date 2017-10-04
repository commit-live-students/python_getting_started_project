from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here

    extra1 = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['runs']['extras'] > 0:
                extra1 = extra1+1

    extra2 = 0
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['runs']['extras'] > 0:
                extra2 = extra2+1

    difference = extra2-extra1

    return difference
