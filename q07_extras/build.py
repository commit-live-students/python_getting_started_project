# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

extra_bowled_first = 0
extra_bowled_second = 0

def get_for_both(innings):
    count = 0
    for item in innings:
        for k,v in item.items():
            new_val = item[k]
            if new_val.has_key('extras'):
                    count = count + 1
    return count

# Your Solution
def extras_runs(data=data):

    # Write your code here
    extra_bowled_first = get_for_both(data['innings'][0]['1st innings']['deliveries'])
    extra_bowled_second = get_for_both(data['innings'][1]['2nd innings']['deliveries'])

    difference = extra_bowled_second - extra_bowled_first
    print difference

    return difference

extras_runs()
