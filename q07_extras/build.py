# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    extras_1, extras_2 = 0, 0
    for delivery in data['innings'][0]['1st innings']['deliveries']:
        delivery_content = delivery[next(iter(delivery))]
        if 'extras' in delivery_content:
            extras_1 += 1
    for delivery in data['innings'][1]['2nd innings']['deliveries']:
        delivery_content = delivery[next(iter(delivery))]
        if 'extras' in delivery_content:
            extras_2 += 1
    difference = extras_2 - extras_1

    return difference
