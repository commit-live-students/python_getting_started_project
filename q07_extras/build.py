# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    extras_inn1, extras_inn2 = 0, 0
    for delivery in data['innings'][0]['1st innings']['deliveries']:
        delivery_content = delivery[next(iter(delivery))]
        if 'extras' in delivery_content:
            extras_inn1 += 1
    for delivery in data['innings'][1]['2nd innings']['deliveries']:
        delivery_content = delivery[next(iter(delivery))]
        if 'extras' in delivery_content:
            extras_inn2 += 1


    difference = extras_inn2 - extras_inn1


    return difference
