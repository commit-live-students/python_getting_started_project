# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def calculate_extras(innings):
    extras = 0
    for item in innings:
        delivery = list(item.values())[0]
        if 'extras' in delivery:
            extras += 1
    
    return extras
# Your Solution
def extras_runs(data=data):

    # Write your code here
    inning_first = data['innings'][0]['1st innings']['deliveries']
    inning_second = data['innings'][1]['2nd innings']['deliveries']
    extra_inning_first = calculate_extras(inning_first)
    extra_inning_second = calculate_extras(inning_second)
    difference = extra_inning_second - extra_inning_first


    return difference

extras_runs()


