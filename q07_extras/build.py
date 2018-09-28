# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    extras_1 = []
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if 'extras' in delivery_info and delivery_info['runs']['extras']:
                extras_1.append(delivery_info['runs']['extras'])
    extras_2 = []
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if 'extras' in delivery_info and delivery_info['runs']['extras']:
                extras_2.append(delivery_info['runs']['extras'])
    difference = (sum(extras_2)) - (sum(extras_1))
    return difference

