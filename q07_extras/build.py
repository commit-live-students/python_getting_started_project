# Default Imports
import pprint
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    extras1=0
    extras2=0
    # Write your code here
    for delivery in data['innings'][0]['1st innings']['deliveries']:


        for key, val in delivery.items():
            if 'extras' in val:
                    extras1= extras1 + 1

    for delivery in data['innings'][1]['2nd innings']['deliveries']:
        for key2, val2 in delivery.items():
            if 'extras' in val2:
                extras2= extras2 + 1


    difference = extras2-extras1
    return difference

extras_runs(data)
