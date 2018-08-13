from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    extras1 = 0
    extras2 = 0

    deliveries1 = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries1:
        for key,value in delivery.items():
            extras1 += value['runs']['extras']

    deliveries2 = data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries2:
        for key,value in delivery.items():
            extras2 += value['runs']['extras']

    difference = extras2 - extras1
    return difference
